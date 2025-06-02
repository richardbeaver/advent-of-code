from pathlib import Path
from python import utils
from . import part1
from . import part2


TEST_INPUT = """7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9"""


def test_part1():
    assert part1.solve(TEST_INPUT) == 2


def test_part2():
    assert part2.solve(TEST_INPUT) == 4

    own_input = """4 6 4 2 1"""
    assert part2.solve(own_input) == 1


# =============


def test_solutions():
    """Test part1 and part2 on full input to ensure they correctly solve puzzle"""
    day: str = Path(__file__).parent.name.removeprefix("day")
    text = utils.read_data_input(int(day))

    assert part1.solve(text) == 680
    assert part2.solve(text) == 710
