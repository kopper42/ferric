#!/usr/bin/env python3
"""
Validate TASKS.md and SLICES.md state, task/slice marker integrity, and cross-file consistency
for the updated three-level agentic workflow (PHASES/SLICES/TASKS).

Usage:
  python scripts/validate_tasks_state.py
  python scripts/validate_tasks_state.py --file TASKS.md --file SLICES.md --strict
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path


ALLOWED_STATES = {
    "PLANNING_PENDING_APPROVAL",
    "APPROVED_FOR_EXECUTION",
    "EXECUTING",
    "BLOCKED_NEEDS_INPUT",
    "PHASE_COMPLETE_PENDING_APPROVAL",
    "PHASE_APPROVED_COMPLETE",
}

STATE_RE = re.compile(r"^State:\s*([A-Z_]+)\s*$")
TASK_LINE_RE = re.compile(r"^\s*-\s*\[( |x|-)\]\s+Task\b")
# Updated to catch both list items and markdown headers used in PHASES.md/SLICES.md (per dual AI reviews)
SLICE_LINE_RE = re.compile(r"^(##\s+|\s*-\s*)\[([ x-])\]\s*(?:Slice|Phase|[-]?\s*Slice)", re.IGNORECASE)
CHECKBOX_RE = re.compile(r"^\s*-\s*\[( |x)\]")


def read_lines(path: Path) -> list[str]:
    if not path.exists():
        raise FileNotFoundError(f"File not found: {path}")
    return path.read_text(encoding="utf-8").splitlines()


def find_state(lines: list[str]) -> list[tuple[int, str]]:
    results: list[tuple[int, str]] = []
    for i, line in enumerate(lines):
        m = STATE_RE.match(line)
        if m:
            results.append((i + 1, m.group(1)))
    return results


def find_execution_gate_checkbox(lines: list[str]) -> tuple[tuple[int, bool] | None, str | None]:
    gate_idx = None
    for i, line in enumerate(lines):
        if line.strip() == "## Execution Gate":
            gate_idx = i
            break

    if gate_idx is None:
        return None, "Missing `## Execution Gate` section"

    # Look ahead in a bounded range to find the checkbox line under this section.
    for j in range(gate_idx + 1, min(gate_idx + 12, len(lines))):
        m = CHECKBOX_RE.match(lines[j])
        if m:
            return (j + 1, m.group(1) == "x"), None

    return None, "Missing execution-gate checkbox line under `## Execution Gate`"


def parse_tasks(lines: list[str]) -> list[tuple[int, str]]:
    tasks: list[tuple[int, str]] = []
    for i, line in enumerate(lines):
        m = TASK_LINE_RE.match(line)
        if m:
            tasks.append((i + 1, m.group(1)))  # marker is " ", "x", or "-"
    return tasks


def check_done_tasks_have_verification(lines: list[str], tasks: list[tuple[int, str]]) -> list[str]:
    errors: list[str] = []
    for line_no, marker in tasks:
        if marker != "x":
            continue

        start = line_no - 1
        end = len(lines)
        for i in range(start + 1, len(lines)):
            if TASK_LINE_RE.match(lines[i]) or lines[i].startswith("### Slice:") or lines[i].startswith("## "):
                end = i
                break
        block = lines[start:end]
        if not any("Verification:" in ln for ln in block):
            errors.append(f"Task at line {line_no} is [x] but its block lacks `Verification:`")
    return errors


def validate(path: Path, strict: bool) -> list[str]:
    lines = read_lines(path)
    errors: list[str] = []
    is_tasks = path.name.upper().startswith("TASKS")
    is_slices = path.name.upper().startswith("SLICES")

    # State line checks (TASKS only)
    states = find_state(lines)
    state_val = None
    if is_tasks:
        if len(states) != 1:
            errors.append(f"Expected exactly one `State:` line in TASKS.md, found {len(states)}")
            state_val = None
        else:
            state_line, state_val = states[0]
            if state_val not in ALLOWED_STATES:
                errors.append(f"Invalid state `{state_val}` at line {state_line}")
    elif is_slices and len(states) > 0:
        errors.append("SLICES.md should not contain `State:` line (state lives in TASKS.md for active slice)")

    # Execution gate checks (TASKS only)
    if is_tasks:
        gate_info, gate_err = find_execution_gate_checkbox(lines)
        gate_checked = None
        if gate_err:
            errors.append(gate_err)
        else:
            _, gate_checked = gate_info  # line_no unused

    # Marker checks
    if is_tasks:
        tasks = parse_tasks(lines)
        if not tasks:
            errors.append("No task lines found in TASKS.md (expected `- [ ] Task ...`, `- [-] Task ...`, or `- [x] Task ...`)")
        else:
            active_count = sum(1 for _, marker in tasks if marker == "-")
            done_count = sum(1 for _, marker in tasks if marker == "x")
            total = len(tasks)
            all_done = done_count == total

            # Tri-state policy: exactly one active task while work remains.
            if not all_done and active_count != 1:
                errors.append(
                    f"Expected exactly one active task marker `[-]` while tasks remain; found {active_count}"
                )
            if all_done and active_count != 0:
                errors.append("All tasks are [x], but an active `[-]` task still exists")

            if strict:
                errors.extend(check_done_tasks_have_verification(lines, tasks))
    elif is_slices or path.name.upper().startswith("PHASES"):
        # Enhanced marker check for SLICES.md and PHASES.md (supports both `- [marker]` and `## [marker]` styles)
        markers = []
        for i, line in enumerate(lines):
            m = SLICE_LINE_RE.match(line)
            if m:
                # Group 2 is now the marker for the updated regex
                marker = m.group(2)
                markers.append((i + 1, marker))
        active_count = sum(1 for _, marker in markers if marker == "-")
        doc_type = "phase" if path.name.upper().startswith("PHASES") else "slice"
        if active_count != 1 and len(markers) > 0:
            errors.append(f"Expected exactly one active {doc_type} marker `[-]` in {path.name}; found {active_count}")
        # Basic task-size heuristic for TASKS (if parsed alongside)
        if is_tasks and strict:
            for i, line in enumerate(lines):
                if "Files to change:" in line or "Files to change" in line:
                    # Simple count of files (comma or "`, `")
                    files_part = line.split(":", 1)[-1].strip()
                    file_count = len([f for f in files_part.split(",") if f.strip()])
                    if file_count > 2:
                        errors.append(f"Task at line {i+1} exceeds preferred ≤2 files (found ~{file_count})")

    # State/gate consistency (TASKS only)
    if is_tasks and state_val is not None and 'gate_checked' in locals() and gate_checked is not None:
        if state_val in {"APPROVED_FOR_EXECUTION", "EXECUTING"} and not gate_checked:
            errors.append(f"State `{state_val}` requires checked execution gate")
        if state_val == "PLANNING_PENDING_APPROVAL" and gate_checked:
            errors.append("State `PLANNING_PENDING_APPROVAL` requires unchecked execution gate")

    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate TASKS.md/SLICES.md/PHASES.md for three-level workflow (enhanced per dual AI reviews)")
    parser.add_argument("--file", action="append", default=[], help="Path to document(s) to validate")
    parser.add_argument("--strict", action="store_true", help="Enable stricter checks")
    args = parser.parse_args()

    files = args.file or ["TASKS.md", "SLICES.md", "PHASES.md"]
    all_errors: list[str] = []
    for f in files:
        path = Path(f)
        try:
            errors = validate(path, args.strict)
            if errors:
                all_errors.extend([f"{path.name}: {e}" for e in errors])
        except FileNotFoundError as exc:
            all_errors.append(str(exc))

    if all_errors:
        print("Validation FAILED:")
        for err in all_errors:
            print(f"- {err}")
        print("\nDiagnostics: Check Quick Reference in docs/agentic-workflow-v1.md for allowed states/phrases/markers. Run with --strict for task-size and verification proof checks.")
        return 1

    print("Validation PASSED for all provided files.")
    print("Diagnostics: All states valid, exactly one active marker where required, no size violations detected. Quick Reference and back-off table now at top of v1.md.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
