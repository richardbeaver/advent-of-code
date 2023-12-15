use anyhow::{Context, Result};

pub fn process(input: &str) -> Result<usize> {
    let mut sum = 0;

    for line in input.lines() {
        let chars: String = line
            .chars()
            .skip_while(|&char| char != ':')
            .skip(2)
            .collect();
        let (winning_numbers, my_numbers) = chars
            .split_once('|')
            .context("Line does not match expected file format.")?;

        let winning_numbers: Vec<_> = winning_numbers.split_whitespace().collect();
        let my_numbers: Vec<_> = my_numbers.split_whitespace().collect();

        let mut score = 0;
        for number in my_numbers {
            if winning_numbers.contains(&number) {
                if score == 0 {
                    score += 1;
                } else {
                    score *= 2;
                }
            }
        }

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
