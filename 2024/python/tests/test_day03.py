from pathlib import Path
import testing_utils


DAY = testing_utils.get_day_from_filename(Path(__file__).name)

TEST_INPUT_1 = """
xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))
"""

TEST_INPUT_2 = """
xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))
"""


def test_sample_part1():
    testing_utils.run_part_test(DAY, part=1, input_text=TEST_INPUT_1, expected=161)


def test_sample_part2():
    testing_utils.run_part_test(DAY, part=2, input_text=TEST_INPUT_2, expected=48)


def test_solutions():
    testing_utils.run_full_input_test(DAY, part=1, expected=196826776)
    testing_utils.run_full_input_test(DAY, part=2, expected=106780429)
