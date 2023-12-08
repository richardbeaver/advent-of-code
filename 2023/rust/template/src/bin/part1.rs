use template::part1::process;

fn main() {
    let input = include_str!("../../input2.txt");
    let output = process(input);
    dbg!(output);
}
