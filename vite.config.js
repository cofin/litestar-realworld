import { defineConfig } from "vite";

import litestar from "litestar-vite-plugin";

export default defineConfig({
  root: "src/realworld/domain/web/resources",
  plugins: [
    litestar({
      input: [
        "src/realworld/domain/web/resources/main.css",
        "src/realworld/domain/web/resources/main.js",
      ],
      assetUrl: "/static/",
      assetDirectory: "src/realworld/domain/web/resources/assets",
      bundleDirectory: "src/realworld/domain/web/public",
      resourceDirectory: "src/realworld/domain/web/resources",
      hotFile: "src/realworld/domain/web/public/hot",
    }),
  ],
  server: {
    port: 3005,
  },
  resolve: {
    alias: {
      "@": "src/realworld/domain/web/resources",
    },
  },
});
