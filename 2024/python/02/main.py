from pathlib import Path
from part1 import part1
from part2 import part2


if __name__ == "__main__":
    current_dir = Path(__file__).resolve()
    day = current_dir.parent.name
    input_file_path = current_dir.parents[2] / "inputs" / f"{day}.txt"

    with open(input_file_path, "r", encoding="utf-8") as input_file:
        text = input_file.read()

    print(part1(text))  # => 680
    print(part2(text))  # => 710
