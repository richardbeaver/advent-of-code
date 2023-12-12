use anyhow::Result;
use std::cmp;

// TODO: replace unwraps with anyhow error handling

/// Get sum of all numbers adjacent to any symbol (even diagonally)
pub fn process(input: &str) -> Result<usize> {
    let mut sum = 0;
    let lines: Vec<_> = input.lines().collect();

    for (line_num, line) in input.lines().enumerate() {
        let mut current_num = String::new();

        for (mut idx, char) in line.chars().enumerate() {
            if char.is_numeric() {
                current_num.push(char);
            }

            if (!char.is_numeric() || idx == line.len() - 1) && !current_num.is_empty() {
                // `idx` is either past the end of a number or on the last digit
                // of a number at the end of a line
                // If at the last char of the line and it is numeric, increment
                // `idx` so we're past the number (the same scenario as reaching
                // a non-numeric char before the end of the line)
                if idx == line.len() - 1 && char.is_numeric() {
                    idx += 1
                }
                if any_adjacent_symbol(&lines, line_num, idx - current_num.len(), idx) {
                    sum += current_num.parse::<usize>()?;
                }
                current_num.clear();
            }
        }
    }

    Ok(sum)
}

/// Determine if there is a symbol adjacent to the number string described by
/// its line number, its index in its line, and its length
fn any_adjacent_symbol(input_lines: &[&str], line_num: usize, idx: usize, end_idx: usize) -> bool {
    let prev_line = cmp::max(line_num as isize - 1, 0) as usize;
    let next_line = cmp::min(line_num + 1, input_lines.len() - 1);

    let min_idx = cmp::max(idx as isize - 1, 0) as usize;
    let end_idx = cmp::min(end_idx + 1, input_lines.first().unwrap().len());

    for &line in &input_lines[prev_line..=next_line] {
        for char in line[min_idx..end_idx].chars() {
            if is_symbol(char) {
                return true;
            }
        }
    }

    false
}

pub fn is_symbol(char: char) -> bool {
    char != '.' && !char.is_numeric()
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

        let result = process(example_input).unwrap();

        assert_eq!(result, expected_output);
    }
}
