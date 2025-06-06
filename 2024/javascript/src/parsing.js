/**
 * @param {string} data
 * @returns {string[]}
 */
function asLines(data) {
  return data
    .trim()
    .split("\n")
    .map((line) => line.trim());
}

/**
 * @param {string} input_data
 * @returns {number[][]}
 */
function groupAsInts(input_data) {
  const lines = asLines(input_data);
  return lines.map((line) => line.split(/\s+/).map((num) => Number(num)));
}

module.exports = { groupAsInts };
