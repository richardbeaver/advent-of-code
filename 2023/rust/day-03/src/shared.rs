use anyhow::{anyhow, Context, Result};

pub fn is_symbol(char: char) -> bool {
    char != '.' && !char.is_numeric()
}

#[derive(Debug)]
pub struct SubstringLocation {
    pub str: String,
    pub line_num: usize,
    pub idx: usize,
    pub end_idx: usize,
}

impl SubstringLocation {
    pub fn new(input_lines: &[&str], line_num: usize, idx: usize, end_idx: usize) -> Result<Self> {
        if end_idx <= idx {
            return Err(anyhow!("End index must be greater than start index."));
        }

        let input_line = *input_lines
            .get(line_num)
            .context("Line number not a valid index into lines.")?;

        Ok(Self {
            str: input_line[idx..end_idx].to_owned(),
            line_num,
            idx,
            end_idx,
        })
    }
}
