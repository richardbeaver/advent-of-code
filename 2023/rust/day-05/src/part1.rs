use anyhow::{Context, Result};

pub fn process(input: &str) -> Result<usize> {
    let (seeds, maps) = input.split_once("\n\n").unwrap();

    let map_strings: Vec<Vec<_>> = maps
        .split("\n\n")
        .map(|map_section| {
            map_section
                .lines()
                .skip(1)
                // .map(|line| {
                //     let line_values: Vec<usize> = line
                //         .split_whitespace()
                //         .map(|num_str| num_str.parse::<usize>().unwrap())
                //         .collect();
                //     let dst_start = *line_values.first().unwrap();
                //     let src_start = *line_values.get(1).unwrap();
                //     let src_length = *line_values.get(2).unwrap();
                //     (dst_start, src_start, src_length)
                // })
                .collect::<Vec<_>>()
        })
        .collect();

    seeds
        .split_whitespace()
        .skip(1)
        .map(|seed| {
            let seed: usize = seed.parse().unwrap();
            get_seed_location(seed, &map_strings)
        })
        .min()
        .context("No minimum location for any seeds")
}

fn get_seed_location(seed: usize, maps: &[Vec<&str>]) -> usize {
    let mut resulting_value = seed;

    for map in maps {
        resulting_value = get_mapped_number(resulting_value, map);
    }

    resulting_value
}

fn get_mapped_number(seed: usize, map: &[&str]) -> usize {
    for line in map {
        let line_values: Vec<_> = line.split_whitespace().collect();
        let dst_start = line_values.first().unwrap().parse::<usize>().unwrap();
        let src_start = line_values.get(1).unwrap().parse::<usize>().unwrap();
        let src_length = line_values.get(2).unwrap().parse::<usize>().unwrap();

        let difference = seed as isize - src_start as isize;

        if difference < 0 {
            continue;
        }

        let difference = difference as usize;

        if difference < src_length {
            return dst_start + difference;
        }
    }

    seed
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test() {
        let example_input = "seeds: 79 14 55 13

seed-to-soil map:
50 98 2
52 50 48

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15

fertilizer-to-water map:
49 53 8
0 11 42
42 0 7
57 7 4

water-to-light map:
88 18 7
18 25 70

light-to-temperature map:
45 77 23
81 45 19
68 64 13

temperature-to-humidity map:
0 69 1
1 0 69

humidity-to-location map:
60 56 37
56 93 4";
        let expected_output = 35;

        let result = process(example_input).unwrap();
        assert_eq!(result, expected_output);
    }
}
