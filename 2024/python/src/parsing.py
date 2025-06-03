from typing import Iterator


# A running collection of functions to help parse problem input. Will be
# interesting to see how this looks later on and how well I'm able to reuse them.


def as_lines(data: str) -> Iterator[str]:
    return map(str.strip, data.strip().splitlines())


def group_as_ints(input_data: str) -> Iterator[Iterator[int]]:
    lines = as_lines(input_data)
    return ((int(num) for num in line.split()) for line in lines)
