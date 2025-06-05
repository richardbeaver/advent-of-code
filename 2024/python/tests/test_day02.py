from pathlib import Path
from testing_utils import get_day_from_filename, run_part_test
import utils

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

# 7 6 4 2 1: Safe because the levels are all decreasing by 1 or 2.
# 1 2 7 8 9: Unsafe because 2 7 is an increase of 5.
# 9 7 6 2 1: Unsafe because 6 2 is a decrease of 4.
# 1 3 2 4 5: Unsafe because 1 3 is increasing but 3 2 is decreasing.
# 8 6 4 4 1: Unsafe because 4 4 is neither an increase or a decrease.
# 1 3 6 7 9: Safe because the levels are all increasing by 1, 2, or 3.


def test_sample_part1():
    run_part_test(DAY, part=1, input_text=SAMPLE_INPUT, expected=2)


def test_sample_part2():
    run_part_test(DAY, part=2, input_text=SAMPLE_INPUT, expected=4)
    run_part_test(DAY, part=2, input_text="4 6 4 2 1", expected=1)


# =============

# 7 6 4 2 1: Safe without removing any level.
# 1 2 7 8 9: Unsafe regardless of which level is removed.
# 9 7 6 2 1: Unsafe regardless of which level is removed.
# 1 3 2 4 5: Safe by removing the second level, 3.
# 8 6 4 4 1: Safe by removing the third level, 4.
# 1 3 6 7 9: Safe without removing any level.


def test_full_input_part1():
    run_part_test(DAY, part=1, input_text=FULL_INPUT, expected=680)


def test_full_input_part2():
    run_part_test(DAY, part=2, input_text=FULL_INPUT, expected=710)
