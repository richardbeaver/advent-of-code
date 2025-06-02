from . import part1


def solve(problem_input: str) -> int:
    grouped_values: list[list[int]] = part1.parse_input(problem_input)

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
