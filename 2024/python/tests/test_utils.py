import re
from types import ModuleType
from typing import Any


def run_solver_test(part_module: ModuleType, input_text: str, expected: Any):
    result = part_module.solve(input_text)
    assert result == expected, f"Expected {expected}, got {result}"


def get_day_from_filename(filename: str) -> int:
    match = re.search(r"day(\d+)", filename)
    if not match:
        raise ValueError(f"Could not extract day from filename: {filename}")
    return int(match.group(1))
