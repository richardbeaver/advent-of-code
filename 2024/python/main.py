import argparse
import importlib.util
from pathlib import Path
import sys
from types import ModuleType
import utils


def get_day_from_args() -> int:
    """Extract the day as an `int` from command line arguments."""
    parser = argparse.ArgumentParser()
    parser.add_argument("day", type=int, help="Day number to run (e.g., 1 for 01)")
    args = parser.parse_args()
    return args.day


def load_module(module_path: Path) -> ModuleType | None:
    """Dynamically import a module from a file path."""
    spec = importlib.util.spec_from_file_location(module_path.stem, module_path)
    if spec is None:
        return None

    module = importlib.util.module_from_spec(spec)
    sys.modules[module_path.stem] = module

    loader = spec.loader
    if loader is None:
        return None
    loader.exec_module(module)

    return module


if __name__ == "__main__":
    day = get_day_from_args()

    input_text = utils.read_input_file(day)
    if input_text is None:
        sys.exit(f"Could not retrieve input file for Day {day}. Exiting...")

    base_dir = Path(__file__).parent
    day_dir = base_dir / f"{day:02}"
    part1_path = day_dir / "part1.py"
    part2_path = day_dir / "part2.py"

    part1 = load_module(part1_path)
    part2 = load_module(part2_path)

    if part1 is None:
        sys.exit(f"Could not find Day {day}, part1 module")
    if part2 is None:
        sys.exit(f"Could not find Day {day}, part2 module")

    print(f"=== Day {day:02} ===")
    print("Part 1:", part1.part1(input_text))
    print("Part 2:", part2.part2(input_text))
