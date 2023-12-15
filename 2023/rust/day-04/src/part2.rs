use anyhow::Result;
use std::collections::HashMap;

pub fn process(input: &str) -> Result<usize> {
    let mut card_counts = HashMap::new();

    for (idx, line) in input.lines().enumerate() {
        let cur_card_number = idx + 1;
        let num_copies = *card_counts.entry(cur_card_number).or_insert(1);

        let num_matches = get_number_of_matches(line);

        for card_number in (cur_card_number + 1)..=(cur_card_number + num_matches) {
            let their_count = card_counts.get(&card_number).unwrap_or(&1);
            card_counts.insert(card_number, their_count + num_copies);
        }
    }

    Ok(card_counts.values().sum())
}

fn get_number_of_matches(line: &str) -> usize {
    let line = line.chars().skip(8).collect::<String>();
    let (winning_numbers, my_numbers) = line.split_once(|num| num == '|').unwrap();

    let winning_numbers: Vec<_> = winning_numbers
        .split_whitespace()
        .map(|num| num.to_owned())
        .collect();
    let my_numbers: Vec<_> = my_numbers
        .split_whitespace()
        .map(|num| num.to_owned())
        .collect();

    my_numbers
        .iter()
        .filter(|num| winning_numbers.contains(num))
        .count()
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
        let expected_output = 30;

        let result = process(example_input).unwrap();
        assert_eq!(result, expected_output);
    }
}
