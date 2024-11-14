/** @type {import("prettier").Config} */
export default {
    plugins: ["prettier-plugin-astro"],
    printWidth: 120,
    tabWidth: 4,
    proseWrap: "always",
    overrides: [
        {
            files: "*.astro",
            options: {
                parser: "astro",
            },
        },
        {
            files: "*.mdx",
        },
    ],
};
