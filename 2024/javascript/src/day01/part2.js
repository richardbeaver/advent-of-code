const parsing = require("../parsing");

/**
 * Tally a `similarity score`, which is the sum of:
    - Every number in the left side list multipled by how many times it appears
      in the right side list
 * @param {string} problemInput
 * @returns {number}
 */
function solve(problemInput) {
  let input_values = parsing.groupAsInts(problemInput);
  let cols = input_values.map((_, colIdx) =>
    input_values.map((row) => row[colIdx])
  );

  let left = cols[0];
  let right = cols[1];

  let rightSideCounts = new Map();
  for (const right_val of right) {
    let curCount = rightSideCounts.get(right_val) || 0;
    rightSideCounts.set(right_val, curCount + 1);
  }

  let total = 0;
  for (const left_val of left) {
    total += left_val * (rightSideCounts.get(left_val) || 0);
  }

  return total;
}

module.exports = { solve };
