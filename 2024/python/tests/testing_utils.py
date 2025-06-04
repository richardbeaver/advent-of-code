import re
from typing import Any
from src import utils


def get_day_from_filename(filename: str) -> int:
    match = re.search(r"day(\d+)", filename)
    if not match:
        raise ValueError(f"Could not extract day from filename: {filename}")
    return int(match.group(1))


def run_part_test(day: int, part: int, input_text: str, expected: Any):
    module = utils.import_part_module(day, part)
    result = module.solve(input_text)
    assert (
        result == expected
    ), f"Day {day}, Part {part} failed: expected {expected}, got {result}"
