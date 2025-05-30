import collections
import os


def form_lists(problem_input: str) -> tuple[list[int], list[int]]:
    input_values = problem_input.split()
    left = [int(value) for value in input_values[::2]]
    right = [int(value) for value in input_values[1::2]]

    return (left, right)


def part1(problem_input: str) -> int:
    left, right = form_lists(problem_input)
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


def test_part1():
    test_input = """3   4
4   3
2   5
1   3
3   9
3   3"""
    assert part1(test_input) == 11


# ==================================================================
# ==================================================================


def part2(problem_input: str) -> int:
    """
    Tally a `similarity score`, which is the sum of:
    - Every number in the left side list multipled by how many times it appears
      in the right side list
    """

    left, right = form_lists(problem_input)

    # 1.

    # Using `List.count()`
    # Linear time to count occurrences in `right` list for each `left` list value
    # Time complexity - O(n^2)

    # return sum(val * right.count(val) for val in left)

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

    # 3.

    # Manually doing what `collections.Counter` does with a `dict`
    # - A `defaultdict` would allow for simpler incrementing, as `[]` access
    #   would return a 0 by default if value was not contained as a key (would
    #   not need `get` method with a default value of `0` for each access)

    right_side_counts: dict[int, int] = {}

    for right_val in right:
        right_side_counts[right_val] = right_side_counts.get(right_val, 0) + 1

    return sum(left_val * right_side_counts.get(left_val, 0) for left_val in left)


def test_part2():
    test_input = """3   4
4   3
2   5
1   3
3   9
3   3"""
    assert part2(test_input) == 31


# ==================================================================
# ==================================================================


if __name__ == "__main__":
    dir_path = os.path.dirname(os.path.abspath(__file__))

    with open(f"{dir_path}/input.txt", "r", encoding="utf-8") as input_file:
        text = input_file.read()

    print(part1(text))  # => 1646452
    print(part2(text))  # => 23609874
