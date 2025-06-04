module.exports = [
  js.configs.recommended,
  {
    files: ["**/*.js"],
    languageOptions: {
      parser: require("@typescript-eslint/parser"),
      parserOptions: {
        ecmaVersion: "latest",
        sourceType: "script",
      },
    },
    plugins: {
      "@typescript-eslint": require("@typescript-eslint/eslint-plugin"),
      jsdoc: require("eslint-plugin-jsdoc"),
      jest,
    },
    env: {
      jest: true, // adds `test`, `expect`, etc. to globals
      node: true,
    },
    extends: ["eslint:recommended", "plugin:jest/recommended"],
    rules: {
      ...jest.configs.recommended.rules,
    },
  },
];
