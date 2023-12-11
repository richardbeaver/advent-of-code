use {{crate_name}}::part1::process;

fn main() {
    let input = include_str!("../../input1.txt");
    let output = process(input);
    dbg!(output);
}
