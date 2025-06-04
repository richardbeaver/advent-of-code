from pathlib import Path
from testing_utils import get_day_from_filename, run_part_test
from src import utils

DAY = get_day_from_filename(Path(__file__).name)
FULL_INPUT = utils.read_data_input(DAY)


SAMPLE_INPUT = """
7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9
"""


# =============


def test_sample_part1():
    run_part_test(DAY, part=1, input_text=SAMPLE_INPUT, expected=2)


def test_sample_part2():
    run_part_test(DAY, part=2, input_text=SAMPLE_INPUT, expected=4)
    run_part_test(DAY, part=2, input_text="4 6 4 2 1", expected=1)


# =============


def test_full_input_part1():
    run_part_test(DAY, part=1, input_text=FULL_INPUT, expected=680)


def test_full_input_part2():
    run_part_test(DAY, part=2, input_text=FULL_INPUT, expected=710)
