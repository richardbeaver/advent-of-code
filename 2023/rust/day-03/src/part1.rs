use std::cmp;

// Get sum of all numbers adjacent to any symbol (even diagonally)
pub fn process(input: &str) -> usize {
    let mut sum = 0;
    let lines: Vec<_> = input.lines().collect();

    let number_locations = get_all_number_locations(&lines);

    dbg!(&number_locations);

    for num_loc in number_locations {
        if any_adjacent_symbol(&lines, num_loc.line, num_loc.idx, num_loc.end_idx) {
            sum += num_loc.number_str.parse::<usize>().unwrap();
        }
    }

    sum
}

#[derive(Debug)]
pub struct NumberStringLocation {
    number_str: String,
    line: usize,
    idx: usize,
    end_idx: usize,
}

impl NumberStringLocation {
    fn new(input_lines: &[&str], line: usize, idx: usize, end_idx: usize) -> Result<Self, ()> {
        if end_idx <= idx {
            return Err(());
        }

        let input_line = *input_lines.get(line).ok_or(())?;

        Ok(Self {
            number_str: input_line[idx..end_idx].to_owned(),
            line,
            idx,
            end_idx,
        })
    }
}

pub fn get_all_number_locations(input_lines: &[&str]) -> Vec<NumberStringLocation> {
    let mut number_locations = Vec::new();

    for (line_num, line) in input_lines.iter().enumerate() {
        let mut i = 0;
        while i < line.len() {
            let next_num: String = line
                .get(i..)
                .unwrap()
                .chars()
                .take_while(|c| c.is_numeric())
                .collect();

            if !next_num.is_empty() {
                let number =
                    NumberStringLocation::new(input_lines, line_num, i, i + next_num.len())
                        .unwrap();
                number_locations.push(number);
            }

            i += cmp::max(next_num.len(), 1);
        }
    }

    number_locations
}

// Determine if there is a symbol adjacent to the number string described by
// its line number, its index in its line, and its length
fn any_adjacent_symbol(input_lines: &[&str], line_num: usize, idx: usize, end_idx: usize) -> bool {
    let last_line = cmp::max(line_num as isize - 1, 0) as usize;
    let next_line = cmp::min(line_num + 1, input_lines.len() - 1);

    let min_idx = cmp::max(idx as isize - 1, 0) as usize;
    let end_idx = cmp::min(end_idx + 1, input_lines.first().unwrap().len());

    for &line in &input_lines[last_line..=next_line] {
        for char in line[min_idx..end_idx].chars() {
            if char != '.' && !char.is_numeric() {
                return true;
            }
        }
    }

    false
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test() {
        let example_input = "467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..";
        let expected_output = 4361;

        let result = process(example_input);

        assert_eq!(result, expected_output);
    }
}
