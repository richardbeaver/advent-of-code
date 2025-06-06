const parsing = require("../parsing");

/**
 * Tally a `similarity score`, which is the sum of:
    - Every number in the left side list multipled by how many times it appears
      in the right side list
 * @param {string} problemInput
 * @returns {number}
 */
function solve(problemInput) {
  const input_values = parsing.groupAsInts(problemInput);
  const cols = input_values.map((_, colIdx) =>
    input_values.map((row) => row[colIdx])
  );

  const left = cols[0];
  const right = cols[1];

  const rightSideCounts = new Map();
  for (const right_val of right) {
    const curCount = rightSideCounts.get(right_val) || 0;
    rightSideCounts.set(right_val, curCount + 1);
  }

  let total = 0;
  for (const left_val of left) {
    total += left_val * (rightSideCounts.get(left_val) || 0);
  }

  return total;
}

module.exports = { solve };
