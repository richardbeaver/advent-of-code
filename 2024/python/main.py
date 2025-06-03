import argparse
import importlib
import sys
import utils


def main(day: int):
    input_text = utils.read_data_input(day)

    print(f"=== Day {day:02} ===")

    # Run part 1 (always required)
    try:
        part1 = importlib.import_module(f"day{day:02}.part1")
        print("Part 1:", part1.solve(input_text))
    except (ImportError, AttributeError) as e:
        print(f"[ERROR] Could not run part 1: {e}")
        return

    # Run part 2 (optional)
    try:
        part2 = importlib.import_module(f"day{day:02}.part2")
        print("Part 2:", part2.solve(input_text))
    except ModuleNotFoundError:
        print("[INFO] Skipping part 2 — not implemented yet.")
    except AttributeError as e:
        print(f"[ERROR] part2 module found but missing 'solve': {e}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("day", type=int)
    args = parser.parse_args()

    main(args.day)

    # try:
    #     main(args.day)
    # except (FileNotFoundError, ImportError) as e:
    #     sys.exit(f"Error: {e}")
