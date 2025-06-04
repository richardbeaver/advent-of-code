import itertools
import parsing


# For each group (row) in the input, it is safe if all differences between
# consecutive values:
#   - are in the same direction (all positive or all negative)
#   - have an absolute value in the range [1, 3]

# Return total number of safe groups


def solve(problem_input: str) -> int:
    input_values = parsing.group_as_ints(problem_input)

    num_safe = 0

    for group in input_values:
        group_diffs = [val2 - val1 for val1, val2 in itertools.pairwise(group)]

        if all(1 <= diff <= 3 for diff in group_diffs) or all(
            -1 >= diff >= -3 for diff in group_diffs
        ):
            num_safe += 1

    return num_safe
