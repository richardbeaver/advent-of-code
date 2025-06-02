from pathlib import Path
import sys
from . import part1
from . import part2


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

sys.path.append(str(Path(__file__).resolve().parents[1]))

from utils import read_data_input


def test_solutions():
    """Test part1 and part2 on full input to ensure they correctly solve puzzle"""
    day: str = Path(__file__).parent.name.removeprefix("day")
    text = read_data_input(int(day))

    assert part1.solve(text) == 1646452
    assert part2.solve(text) == 23609874
