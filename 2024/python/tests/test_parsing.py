from parsing import as_lines, group_as_ints


TEST_INPUT = """
3   4
4   3
2   5
1   3
3   9
3   3"""


def test_as_lines():
    lines = as_lines(TEST_INPUT)
    assert list(lines) == ["3   4", "4   3", "2   5", "1   3", "3   9", "3   3"]


def test_group_as_ints():
    grouped = group_as_ints(TEST_INPUT)
    as_lists = list(list(row) for row in grouped)
    assert as_lists == [[3, 4], [4, 3], [2, 5], [1, 3], [3, 9], [3, 3]]
