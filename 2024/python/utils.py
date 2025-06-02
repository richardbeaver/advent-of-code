from pathlib import Path


def read_data_input(day: int) -> str:
    """Return the string of text from the input file for the provided day"""
    input_file_path = Path(__file__).parent.parent / "inputs" / f"day{day:02}.txt"
    try:
        return input_file_path.read_text()
    except FileNotFoundError as e:
        raise FileNotFoundError(f"Data input file not found for day {day:02}") from e
