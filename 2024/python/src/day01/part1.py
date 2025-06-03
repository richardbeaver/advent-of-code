import parsing


def solve(problem_input: str) -> int:
    """
    Tally a 'total distance':
    - The sum of all distances between each pair of numbers in the two lists,
      after having been sorted
    """
    input_values = parsing.group_as_ints(problem_input)
    left, right = (list(col) for col in zip(*input_values))

    left.sort()
    right.sort()

    # ===

    # 1. Using a for-loop to iterate over the pairs and manually summing a total
    # total_distance = 0
    # for i, left_val in enumerate(left):
    #     total_distance += abs(left_val - right[i])

    # return total_distance

    # ===

    # 2. As the `sum` of a generator expression
    return sum(abs(left_val - right_val) for left_val, right_val in zip(left, right))
