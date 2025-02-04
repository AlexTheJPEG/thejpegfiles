import { defineConfig } from "astro/config";

import remarkObsidian from "remark-obsidian";

import tailwind from "@astrojs/tailwind";

import icon from "astro-icon";

import cloudflare from "@astrojs/cloudflare";

export default defineConfig({
    integrations: [tailwind(), icon()],
    output: "server",
    adapter: cloudflare(),
    markdown: {
        remarkPlugins: [[remarkObsidian, {}]],
    },
});
