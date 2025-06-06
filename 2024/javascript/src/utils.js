const path = require("path");
const fs = require("fs");

/**
 * Return the string of text from the input file for the provided day
 * @param {number} day
 * @returns {string}
 */
function readDataInput(day) {
  const inputFilePath =
    path.resolve(__dirname, "..", "..") +
    `/inputs/day${String(day).padStart(2, "0")}.txt`;

  return fs.readFileSync(inputFilePath, "utf-8");
}

/**
 * Import the `solve` function in the module for the given day and part
 * @param {number} day
 * @param {number} part
 * @returns {(inputText: string) => number}
 */
function importPartSolveFunction(day, part) {
  const filePath = `./day${String(day).padStart(2, "0")}/part${part}`;
  return require(filePath).solve;
}

module.exports = { readDataInput, importPartSolveFunction };
