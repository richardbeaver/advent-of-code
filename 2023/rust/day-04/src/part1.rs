use crate::part2::get_number_of_matches;
use anyhow::Result;

pub fn process(input: &str) -> Result<usize> {
    let mut sum = 0;

    for line in input.lines() {
        let num_matches = get_number_of_matches(line);

        let score = if num_matches == 0 {
            0
        } else {
            2usize.pow((num_matches - 1) as u32)
        };

        sum += score;
    }
    Ok(sum)
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test() {
        let example_input = "Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11";
        let expected_output = 13;

        let result = process(example_input).unwrap();
        assert_eq!(result, expected_output);
    }
}
