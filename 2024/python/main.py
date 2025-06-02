import argparse
import importlib
import sys
import utils


def main(day: int):
    input_text = utils.read_data_input(day)
    part1 = importlib.import_module(f"day{day:02}.part1")
    part2 = importlib.import_module(f"day{day:02}.part2")

    print(f"=== Day {day:02} ===")
    print("Part 1:", part1.solve(input_text))
    print("Part 2:", part2.solve(input_text))


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("day", type=int)
    args = parser.parse_args()

    try:
        main(args.day)
    except (FileNotFoundError, ImportError) as e:
        sys.exit(f"Error: {e}")
