import re
from pathlib import Path
import utils
from day01 import part1, part2


TEST_INPUT = """3   4
4   3
2   5
1   3
3   9
3   3"""


def test_part1():
    """Test part1 using example input"""
    assert part1.solve(TEST_INPUT) == 11


def test_part2():
    """Test part2 using example input"""
    assert part2.solve(TEST_INPUT) == 31


# =============


def test_solutions():
    """Test part1 and part2 on full input to ensure they correctly solve puzzle"""
    file_name = Path(__file__).name
    day = re.search(r"day(\d+)", file_name)
    assert day is not None, f"Could not extract day from filename: {__file__}"

    text = utils.read_data_input(int(day.group(1)))

    assert part1.solve(text) == 1646452
    assert part2.solve(text) == 23609874
