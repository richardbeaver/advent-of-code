use anyhow::Result;
use {{crate_name}}::part1::process;

fn main() -> Result<()> {
    let input = include_str!("../../input1.txt");
    let output = process(input)?;
    dbg!(output);
    Ok(())
}
