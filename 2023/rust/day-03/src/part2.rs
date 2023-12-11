use crate::shared::{is_symbol, SubstringLocation};
use anyhow::{Context, Result};
use std::cmp;

/// For all symbols that are adjacent to exactly two numbers, multiply the
/// two numbers and get sum of all resulting products
pub fn process(input: &str) -> Result<usize> {
    // For every symbol in the input, check the 9 coordinates around it
    // Numbers can be adjacent in 4 directions (above, left, right, below)
    // There can be two adjacent numbers above or below if the coordinate
    // directly above/below the symbol is a period, and the characters to the
    // left and right of that period are numeric

    let mut sum = 0;

    let lines: Vec<_> = input.lines().collect();
    let symbol_locations = get_all_symbol_locations(&lines);

    for symbol_loc in symbol_locations {
        let adjacent_numbers = get_adjacent_numbers(
            &lines,
            symbol_loc.line_num,
            symbol_loc.idx,
            symbol_loc.end_idx,
        )?;
        if adjacent_numbers.len() == 2 {
            let product: usize = adjacent_numbers.iter().product();
            sum += product;
        }
    }

    Ok(sum)
}

/// Collect substring location structs for all symbols
fn get_all_symbol_locations(input_lines: &[&str]) -> Vec<SubstringLocation> {
    let mut symbol_locations = Vec::new();

    for (line_num, line) in input_lines.iter().enumerate() {
        for (idx, char) in line.chars().enumerate() {
            if is_symbol(char) {
                let symbol_location =
                    SubstringLocation::new(input_lines, line_num, idx, idx + 1).unwrap();
                symbol_locations.push(symbol_location);
            }
        }
    }

    symbol_locations
}

// TODO: convert input lines to 2D vec of characters from the start?
//  eliminates need to index into strings or creating character iterators
//  with `chars()` method

// TODO: use inclusive end indexes for line and line indexes here and
//  in `get_num_from_digit` -> more unified in using inclusive indexing
//  everywhere (lines and line indexes)

/// Collect all numbers adjacent to the substring at the given line number
/// and indexes.
fn get_adjacent_numbers(
    input_lines: &[&str],
    line_num: usize,
    idx: usize,
    end_idx: usize,
) -> Result<Vec<usize>> {
    let prev_line = cmp::max(line_num as isize - 1, 0) as usize;
    let next_line = cmp::min(line_num + 1, input_lines.len() - 1);

    let min_idx = cmp::max(idx as isize - 1, 0) as usize;
    let end_idx = cmp::min(end_idx + 1, input_lines.first().unwrap().len());

    let mut numbers = Vec::new();

    for &line in &input_lines[prev_line..=next_line] {
        let chars = line.chars().collect::<Vec<_>>();

        let mut i = min_idx;
        let mut prev_num = None;

        while i < end_idx {
            let char = chars
                .get(i)
                .context("Invalid index into line of characters.")?;
            if char.is_numeric() {
                let num = get_num_from_digit(line, i)?;
                if Some(num) == prev_num {
                    i += 1;
                    continue;
                }
                numbers.push(num);
                prev_num = Some(num);
            }
            i += 1;
        }
    }

    Ok(numbers)
}

/// Starting from a known digit in a line, find all digits that make up the
/// complete number. Return the numeric value.
fn get_num_from_digit(line: &str, idx: usize) -> Result<usize> {
    let bytes = line.as_bytes();

    // Go left until reaching the end of the number's characters
    let mut start_idx = idx;
    loop {
        if !(bytes[start_idx] as char).is_numeric() {
            start_idx += 1;
            break;
        }
        if start_idx == 0 {
            break;
        }
        start_idx -= 1;
    }

    // Go right until reaching the end of the number's characters
    let mut end_idx = idx;
    loop {
        if end_idx == line.len() {
            break;
        }
        if !(bytes[end_idx] as char).is_numeric() {
            break;
        }
        end_idx += 1;
    }

    let num = line[start_idx..end_idx].parse::<usize>()?;
    Ok(num)
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
        let expected_output = 467835;

        let result = process(example_input).unwrap();

        assert_eq!(result, expected_output);
    }
}
