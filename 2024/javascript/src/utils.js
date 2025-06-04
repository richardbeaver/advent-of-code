const path = require("path");
const fs = require("fs");

/**
 * Return the string of text from the input file for the provided day
 * @param {number} day
 * @returns {string}
 */
function readDataInput(day) {
  let inputFilePath =
    path.resolve(__dirname, "..", "..") +
    `/inputs/day${String(day).padStart(2, "0")}.txt`;

  return fs.readFileSync(inputFilePath, "utf-8");
}

module.exports = { readDataInput };
