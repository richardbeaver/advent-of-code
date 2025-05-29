import os


def part1(problem_input: str) -> int:
    input_values = problem_input.split()
    left = [int(value) for value in input_values[::2]]
    right = [int(value) for value in input_values[1::2]]

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


if __name__ == "__main__":
    dir_path = os.path.dirname(os.path.abspath(__file__))

    with open(f"{dir_path}/input.txt", "r", encoding="utf-8") as input_file:
        text = input_file.read()

    print(part1(text))  # => 1646452
