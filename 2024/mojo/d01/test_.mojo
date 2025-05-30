from testing import *
from part1 import part1
from part2 import part2


var TEST_INPUT = """3   4
4   3
2   5
1   3
3   9
3   3"""


def test_part1():
    assert_equal(part1(TEST_INPUT), 11)


def test_part2():
    assert_equal(part2(TEST_INPUT), 31)
