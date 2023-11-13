module.exports = {
  content: [
    "src/realworld/domain/web/{resources,templates}/**/*.{js,jsx,ts,tsx,vue,j2,html}",
  ],
  theme: {
    extend: {},
  },
  plugins: [require("@tailwindcss/forms"), require("@tailwindcss/typography")],
};
