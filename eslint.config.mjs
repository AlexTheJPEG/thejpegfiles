import eslintPluginAstro from "eslint-plugin-astro";
import eslintConfigPrettier from "eslint-config-prettier";

export default [
    eslintConfigPrettier,
    ...eslintPluginAstro.configs["flat/recommended"], // In CommonJS, the `flat/` prefix is required.
    {
        files: ["*.astro"],
        parser: "astro-eslint-parser",
        parserOptions: {
            parser: "@typescript-eslint/parser",
            extraFileExtensions: [".astro"],
        },
        rules: {
            // override/add rules settings here, such as:
            // "astro/no-set-html-directive": "error"
        },
    },
];
