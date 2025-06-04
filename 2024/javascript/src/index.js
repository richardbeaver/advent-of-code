const utils = require("./utils");

/**
 * @returns {number}
 */
function getDayFromArgs() {
  if (process.argv.length !== 3) {
    console.error("Usage: node src/index.js <day>");
    process.exit(1);
  }

  const day = Number(process.argv[2]);

  if (Number.isNaN(day)) {
    console.error("Invalid 'day' argument. Please provide a number");
    process.exit(1);
  }

  return day;
}

/**
 * Import the `solve` function in the module for the given day and part
 * @param {number} day
 * @param {number} part
 * @returns {any}
 */
function importPartSolveFunction(day, part) {
  const filePath = `./day${String(day).padStart(2, "0")}/part${part}`;
  return require(filePath).solve;
}

function main() {
  const day = getDayFromArgs();
  const inputText = utils.readDataInput(day);

  console.log(`=== Day ${String(day).padStart(2, "0")} ===`);

  // Run part 1 (always required)
  try {
    const part1Solve = importPartSolveFunction(day, 1);
    console.log("Part 1: ", part1Solve(inputText));
  } catch (e) {
    console.error(`Could not run part 1: ${e}`);
    process.exit(1);
  }

  // Run part 2 (optional)
  try {
    const part2Solve = importPartSolveFunction(day, 2);
    console.log("Part 2: ", part2Solve(inputText));
  } catch (e) {
    console.log("[INFO] Skipping part 2 — not implemented yet.");
  }
}

main();
