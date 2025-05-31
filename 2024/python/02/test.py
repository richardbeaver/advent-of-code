from part1 import part1
from part2 import part2


TEST_INPUT = """7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9"""


def test_part1():
    assert part1(TEST_INPUT) == 2


def test_part2():
    assert part2(TEST_INPUT) == 4

    own_input = """4 6 4 2 1"""
    assert part2(own_input) == 1
