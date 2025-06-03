from pathlib import Path
import test_utils
from src import utils
from src.day01 import part1, part2


TEST_INPUT = """3   4
4   3
2   5
1   3
3   9
3   3"""


def test_samples():
    test_utils.run_solver_test(part1, TEST_INPUT, 11)

    test_utils.run_solver_test(part2, TEST_INPUT, 31)


def test_solutions():
    day = test_utils.get_day_from_filename(Path(__file__).name)
    text = utils.read_data_input(day)

    test_utils.run_solver_test(part1, text, 1646452)
    test_utils.run_solver_test(part2, text, 23609874)
