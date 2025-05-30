fn part1(problem_input: String) raises -> Int:
    left, right = form_lists(problem_input)
    sort(left)
    sort(right)

    var total_distance = 0
    for i in range(len(left)):
        total_distance += abs(left[i] - right[i])

    return total_distance


fn form_lists(problem_input: String) raises -> Tuple[List[Int], List[Int]]:
    values = problem_input.split()

    var left = [atol(value[]) for value in values[::2]]
    var right = [atol(value[]) for value in values[1::2]]

    return (left, right)
