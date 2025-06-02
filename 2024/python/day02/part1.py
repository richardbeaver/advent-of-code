import itertools


def solve(problem_input: str) -> int:
    grouped_values = parse_input(problem_input)

    num_safe = 0

    for group in grouped_values:
        group_diffs = [val2 - val1 for val1, val2 in itertools.pairwise(group)]

        if all(1 <= diff <= 3 for diff in group_diffs) or all(
            -1 >= diff >= -3 for diff in group_diffs
        ):
            num_safe += 1

    return num_safe


def parse_input(problem_input: str) -> list[list[int]]:
    lines = problem_input.splitlines()
    return [[int(val) for val in group.split()] for group in lines]
