use anyhow::Result;
use day_03::part2::process;

fn main() -> Result<()> {
    let input = include_str!("../../input2.txt");
    let output = process(input)?;
    dbg!(output);
    Ok(())
    // => 84584891
}
