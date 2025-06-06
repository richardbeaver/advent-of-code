const js = require("@eslint/js");
const jsdoc = require("eslint-plugin-jsdoc");
const jest = require("eslint-plugin-jest");
const globals = require("globals");

module.exports = [
  js.configs.recommended,
  {
    files: ["**/*.js"],
    languageOptions: {
      ecmaVersion: "latest",
      sourceType: "module",
      globals: {
        ...globals.node,
        ...globals.jest,
      },
    },
    plugins: {
      jsdoc,
      jest,
    },
    rules: {
      // JS
      "no-var": "error",
      "prefer-const": "error",
      "no-unused-vars": ["error", { argsIgnorePattern: "^_" }],

      // JSDoc
      "jsdoc/require-jsdoc": "error",
      "jsdoc/require-param": "error",
      "jsdoc/require-returns": "error",
      "jsdoc/check-types": "error",
      "jsdoc/no-undefined-types": "error",
      "jsdoc/require-param-type": "error",
      "jsdoc/require-returns-type": "error",

      ...jest.configs.recommended.rules,
    },
  },
];
