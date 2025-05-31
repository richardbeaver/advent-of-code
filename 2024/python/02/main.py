import os
from part1 import part1
from part2 import part2


if __name__ == "__main__":
    dir_path = os.path.dirname(os.path.abspath(__file__))

    with open(f"{dir_path}/../inputs/02.txt", "r", encoding="utf-8") as input_file:
        text = input_file.read()

    print(part1(text))  # => 680
    print(part2(text))  # => 710
