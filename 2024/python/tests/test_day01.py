from pathlib import Path
import testing_utils

DAY = testing_utils.get_day_from_filename(Path(__file__).name)


TEST_INPUT = """
3   4
4   3
2   5
1   3
3   9
3   3
"""


# =============


def test_sample_part1():
    testing_utils.run_part_test(DAY, part=1, input_text=TEST_INPUT, expected=11)


def test_sample_part2():
    testing_utils.run_part_test(DAY, part=2, input_text=TEST_INPUT, expected=31)


# =============


def test_full_input_part1():
    testing_utils.run_full_input_test(DAY, part=1, expected=1646452)


def test_full_input_part2():
    testing_utils.run_full_input_test(DAY, part=2, expected=23609874)
