import itertools
import parsing


# For each group (row) in the input, it is safe if:
# 1. all differences between values:
#      - are in the same direction (all positive or all negative)
#      - have an absolute value in the range [1, 3]
# OR
# 2. at most 1 element can removed and the group satisfies these conditions

# Return total number of safe groups


def solve(problem_input: str) -> int:
    input_values = parsing.group_as_ints(problem_input)
    return sum(
        1 for group in input_values if safe_as_is(group) or safe_except_one(group)
    )


def safe_as_is(group: list[int]) -> bool:
    """Check if group satisfies the safe conditions with all given values"""
    diffs = [b - a for a, b in itertools.pairwise(group)]

    if all(diff > 0 for diff in diffs):
        increasing = True
    elif all(diff < 0 for diff in diffs):
        increasing = False
    else:
        return False

    if increasing:
        return all(diff in (1, 2, 3) for diff in diffs)
    return all(diff in (-3, -2, -1) for diff in diffs)


def safe_except_one(group: list[int]) -> bool:
    """Check if excluding any values causes the group to satisfy the safe conditions"""
    for i in range(len(group)):
        if safe_as_is(group[:i] + group[i + 1 :]):
            return True
    return False
