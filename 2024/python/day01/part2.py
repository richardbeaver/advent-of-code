from collections import defaultdict
from . import part1


def part2(problem_input: str) -> int:
    """
    Tally a `similarity score`, which is the sum of:
    - Every number in the left side list multipled by how many times it appears
      in the right side list
    """

    left, right = part1.parse_input(problem_input)

    # 1.

    # Using `List.count()`
    # Linear time to count occurrences in `right` list for each `left` list value
    # Time complexity - O(n^2)

    # return sum(val * right.count(val) for val in left)

    # ===

    # 2.

    # Using `collections.Counter`
    #   - Create dictionary from the right side list, mapping each value to the
    #     number of times it appears
    #     - Linear time operation
    #   - Constant time to lookup each left side list value in the dictionary
    #     - Constant time for each list value => linear time overall
    # Time complexity - O(2 * n) => O(n)
    # Note: `[]` access into `Counter` object returns 0 if value is not contained

    # right_side_counts = collections.Counter(right)
    # return sum(left_val * right_side_counts[left_val] for left_val in left)

    # ===

    # 3.

    # Manually doing what `collections.Counter` does with a `dict`

    # right_side_counts: dict[int, int] = {}
    # for right_val in right:
    #     right_side_counts[right_val] = right_side_counts.get(right_val, 0) + 1

    # return sum(left_val * right_side_counts.get(left_val, 0) for left_val in left)

    # ===

    # 4.

    # Same as 3., but using a default dict, which allows for slightly simpler
    # accessing

    right_side_counts: defaultdict[int, int] = defaultdict(int)
    for right_val in right:
        right_side_counts[right_val] += 1

    return sum(left_val * right_side_counts[left_val] for left_val in left)
