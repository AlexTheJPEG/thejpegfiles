import { defineCollection, z } from "astro:content";

import { glob } from "astro/loaders";

const blog = defineCollection({
    loader: glob({ pattern: "**/*.md", base: "./src/content" }),
    schema: z.object({
        title: z.string(),
        slug: z.string(),
        tags: z.array(z.string()),
        dateCreated: z.coerce.date(),
        dateUpdated: z.coerce.date().optional(),
        excerpt: z.string(),
    }),
});

export const collections = { blog };
