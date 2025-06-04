const part1 = require("../src/day01/part1");
const part2 = require("../src/day01/part2");
const utils = require("../src/utils");

const DAY = 1;

const TEST_INPUT = `
3   4
4   3
2   5
1   3
3   9
3   3
`;

// ========

test("sample - part1", () => {
  expect(part1.solve(TEST_INPUT)).toBe(11);
});

test("sample - part2", () => {
  expect(part2.solve(TEST_INPUT)).toBe(31);
});

// ========

let input_text = utils.readDataInput(DAY);

test("full input - part1", () => {
  expect(part1.solve(input_text)).toBe(1646452);
});

test("full input - part2", () => {
  expect(part2.solve(input_text)).toBe(23609874);
});
