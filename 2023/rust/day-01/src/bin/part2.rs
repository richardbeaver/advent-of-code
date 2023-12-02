fn main() {
    let input = include_str!("../../input2.txt");
    let output = part2(input);
    dbg!(output);
}

fn part2(_input: &str) -> String {
    todo!()
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test() {
        let example_input = "";
        let expected_output = "";

        let result = part2(example_input);

        assert_eq!(result, expected_output);
    }
}
