import os
from pathlib import Path
import sys
from part1 import part1
from part2 import part2


TEST_INPUT = """3   4
4   3
2   5
1   3
3   9
3   3"""


def test_part1():
    """Test part1 using example input"""
    assert part1(TEST_INPUT) == 11


def test_part2():
    """Test part2 using example input"""
    assert part2(TEST_INPUT) == 31


# =============

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from utils import read_input_file


def test_solutions():
    """Test part1 and part2 on full input to ensure they correctly solve puzzle"""
    day = Path(__file__).parent.name
    text = read_input_file(day)

    assert part1(text) == 1646452
    assert part2(text) == 23609874
