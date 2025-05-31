from main import part1
from main import part2


TEST_INPUT = """3   4
4   3
2   5
1   3
3   9
3   3"""


def test_part1():
    assert part1(TEST_INPUT) == 11


def test_part2():
    assert part2(TEST_INPUT) == 31
