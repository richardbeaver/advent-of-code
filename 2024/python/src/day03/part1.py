import re


# Find all substrings that follow a pattern of "mul(<num>,<num>)"
# Find the sum of multiplying each pair of numbers in the matching patternss


def solve(problem_input: str) -> int:
    pairs = re.findall(r"mul\((\d+),(\d+)\)", problem_input)
    return sum(int(a) * int(b) for a, b in pairs)
