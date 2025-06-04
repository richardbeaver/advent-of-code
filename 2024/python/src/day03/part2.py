import re


# Two new commands to handle:
#   - do() - enables future mul instructions
#   - don't() - disables future mul instructions
# Only the most recent `do()` or `don't()` instruction applies


def solve(problem_input: str) -> int:
    all_command_pattern = r"mul\((\d+),(\d+)\)|do\(\)|don't\(\)"

    matches = re.finditer(all_command_pattern, problem_input)
    ordered_commands = [match.group() for match in matches]

    total = 0
    do = True
    for command in ordered_commands:
        match command:
            case "do()":
                do = True
            case "don't()":
                do = False
            case _:
                if not do:
                    continue
                num1, num2 = re.findall(r"\d+", command)
                total += int(num1) * int(num2)

    return total
