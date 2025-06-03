from pathlib import Path
import test_utils
import utils
from day02 import part1, part2


TEST_INPUT = """7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9"""


def test_samples():
    test_utils.run_solver_test(part1, TEST_INPUT, 2)

    test_utils.run_solver_test(part2, TEST_INPUT, 4)
    test_utils.run_solver_test(part2, "4 6 4 2 1", 1)


def test_solutions():
    day = test_utils.get_day_from_filename(Path(__file__).name)
    text = utils.read_data_input(day)

    test_utils.run_solver_test(part1, text, 680)
    test_utils.run_solver_test(part2, text, 710)
