from pathlib import Path
from testing_utils import get_day_from_filename, run_part_test
import utils

DAY = get_day_from_filename(Path(__file__).name)
FULL_INPUT = utils.read_data_input(DAY)


SAMPLE_INPUT_PART_1 = """
xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))
"""

SAMPLE_INPUT_PART_2 = """
xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))
"""


# =============


def test_sample_part1():
    run_part_test(DAY, part=1, input_text=SAMPLE_INPUT_PART_1, expected=161)


def test_sample_part2():
    run_part_test(DAY, part=2, input_text=SAMPLE_INPUT_PART_2, expected=48)


# =============


def test_full_input_part1():
    run_part_test(DAY, part=1, input_text=FULL_INPUT, expected=196826776)


def test_full_input_part2():
    run_part_test(DAY, part=2, input_text=FULL_INPUT, expected=106780429)
