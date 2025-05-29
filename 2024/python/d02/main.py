import os
import itertools


def form_data(problem_input: str) -> list[list[int]]:
    lines = problem_input.splitlines()
    return [[int(val) for val in group.split()] for group in lines]


def part1(problem_input: str) -> int:
    grouped_values = form_data(problem_input)

    num_safe = 0

    for group in grouped_values:
        group_diffs = [val2 - val1 for val1, val2 in itertools.pairwise(group)]

        if all(1 <= diff <= 3 for diff in group_diffs) or all(
            -1 >= diff >= -3 for diff in group_diffs
        ):
            num_safe += 1

    return num_safe


def test_part1():
    test_input = """7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9"""
    assert part1(test_input) == 2


# ==================================================================
# ==================================================================


def part2(problem_input: str) -> int:
    grouped_values: list[list[int]] = form_data(problem_input)

    return sum(1 for group in grouped_values if group_is_safe(group))


# TODO: reformulate this -> checking both directions in case first value is the
# one that can be removed. This can probably be done differently without having
# to go through entire group twice
def group_is_safe(group: list[int]) -> bool:
    return group_is_safe_directionally(group) or group_is_safe_directionally(
        group[::-1]
    )


def group_is_safe_directionally(group: list[int]) -> bool:
    """
    Group is safe in this order if at most 1 value can be removed from group
    and all diffs be within [-3, -1] or [1, 3]
    """

    num_removed = 0

    if group[1] - group[0] == 0:
        group = group[1:]
        num_removed += 1

    is_increasing = (group[1] - group[0]) > 0

    i = 0
    while i < len(group) - 1:
        diff = group[i + 1] - group[i]

        if diff_ok(diff, is_increasing):
            pass
        else:
            if num_removed > 0:
                return False

            group = group[::]
            group[i + 1] = group[i]
            num_removed += 1

        i += 1

    return True


def diff_ok(diff: int, is_increasing: bool) -> bool:
    return ((diff > 0) == is_increasing) and 1 <= abs(diff) <= 3


def test_part2():
    test_input = """7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9"""
    assert part2(test_input) == 4

    own_input = """4 6 4 2 1
"""
    assert part2(own_input) == 1


# ==================================================================
# ==================================================================

if __name__ == "__main__":
    dir_path = os.path.dirname(os.path.abspath(__file__))

    with open(f"{dir_path}/input.txt", "r", encoding="utf-8") as input_file:
        text = input_file.read()

    print(part1(text))  # => 680
    print(part2(text))  # => 710
