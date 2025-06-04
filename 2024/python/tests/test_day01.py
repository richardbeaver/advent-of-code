from pathlib import Path
from testing_utils import get_day_from_filename, run_part_test
from src import utils

DAY = get_day_from_filename(Path(__file__).name)
FULL_INPUT = utils.read_data_input(DAY)


SAMPLE_INPUT = """
3   4
4   3
2   5
1   3
3   9
3   3
"""


# =============


def test_sample_part1():
    run_part_test(DAY, part=1, input_text=SAMPLE_INPUT, expected=11)


def test_sample_part2():
    run_part_test(DAY, part=2, input_text=SAMPLE_INPUT, expected=31)


# =============


def test_full_input_part1():
    run_part_test(DAY, part=1, input_text=FULL_INPUT, expected=1646452)


def test_full_input_part2():
    run_part_test(DAY, part=2, input_text=FULL_INPUT, expected=23609874)
