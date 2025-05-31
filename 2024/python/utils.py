from pathlib import Path


def read_input_file(day: int) -> str | None:
    """Return the string of text from the input file for the provided day"""
    current_dir = Path(__file__).resolve()
    input_file_path = current_dir.parents[1] / "inputs" / f"{day:02}.txt"

    try:
        with open(input_file_path, "r", encoding="utf-8") as input_file:
            text = input_file.read()
    except FileNotFoundError:
        print(f"[ERROR]: Input file not found: {input_file_path}")
        return None

    return text
