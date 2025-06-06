const parsing = require("../parsing");

/**
 * Tally a 'total distance':
    - The sum of all distances between each pair of numbers in the two lists,
      after having been sorted
 * @param {string} problemInput
 * @returns {number}
 */
function solve(problemInput) {
  const input_values = parsing.groupAsInts(problemInput);
  const cols = input_values.map((_row, colIdx) =>
    input_values.map((row) => row[colIdx])
  );

  const left = cols[0];
  const right = cols[1];

  left.sort((a, b) => a - b);
  right.sort((a, b) => a - b);

  let sum = 0;
  for (let i = 0; i < left.length; i++) {
    sum += Math.abs(left[i] - right[i]);
  }

  return sum;
}

module.exports = { solve };
