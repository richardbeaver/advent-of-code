from part1 import part1
from part2 import part2


def main():
    var text: String
    with open("inputs/d01.txt", "r'") as file:
        text = file.read()

    print(part1(text))  # => 1646452
    print(part2(text))  # => 23609874
