from pathlib import Path
import testing_utils


DAY = testing_utils.get_day_from_filename(Path(__file__).name)

TEST_INPUT = """
7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9
"""


def test_sample_part1():
    testing_utils.run_part_test(DAY, part=1, input_text=TEST_INPUT, expected=2)


def test_sample_part2():
    testing_utils.run_part_test(DAY, part=2, input_text=TEST_INPUT, expected=4)
    testing_utils.run_part_test(DAY, part=2, input_text="4 6 4 2 1", expected=1)


def test_solutions():
    testing_utils.run_full_input_test(DAY, part=1, expected=680)
    testing_utils.run_full_input_test(DAY, part=2, expected=710)
