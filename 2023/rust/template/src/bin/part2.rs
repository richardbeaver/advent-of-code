use anyhow::Result;
use {{crate_name}}::part2::process;

fn main() -> Result<()> {
    let input = include_str!("../../input2.txt");
    let output = process(input)?;
    dbg!(output);
    Ok(())
}
