const part1 = require("../src/day01/part1");
const part2 = require("../src/day01/part2");
const utils = require("../src/utils");
const testing_utils = require("./testing_utils");
const path = require("path");

const DAY = testing_utils.getDayFromFileName(path.basename(__filename));
const FULL_INPUT = utils.readDataInput(DAY);

const SAMPLE_INPUT = `
3   4
4   3
2   5
1   3
3   9
3   3
`;

// ========

test("sample - part1", () => {
  expect(part1.solve(SAMPLE_INPUT)).toBe(11);
});

test("sample - part2", () => {
  expect(part2.solve(SAMPLE_INPUT)).toBe(31);
});

// ========

test("full input - part1", () => {
  expect(part1.solve(FULL_INPUT)).toBe(1646452);
});

test("full input - part2", () => {
  expect(part2.solve(FULL_INPUT)).toBe(23609874);
});
