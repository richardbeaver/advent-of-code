from part1 import form_lists


fn part2(problem_input: String) raises -> Int:
    left, right = form_lists(problem_input)

    var right_side_counts: Dict[Int, Int] = {}
    for right_val in right:
        var cur_count = right_side_counts.get(right_val[], 0)
        right_side_counts[right_val[]] = cur_count + 1

    total = 0
    for left_val in left:
        total += left_val[] * right_side_counts.get(left_val[], 0)

    return total
