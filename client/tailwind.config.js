const defaultTheme = require('tailwindcss/defaultTheme')
module.exports = {
  // Uncomment the line below to enable the experimental Just-in-Time ("JIT") mode.
  // https://tailwindcss.com/docs/just-in-time-mode
  // mode: "jit",
  theme: {
    extend: {},
    screens: {
      'xs': '475px',
      ...defaultTheme.screens,
      '3xl': '1600px',
      '4xl':'1920px'
    },
  },
  variants: {
    extend: {
      // ...
      outline: ["hover", "active"]
    }
  },
  plugins: [],
  purge: {
    // Filenames to scan for classes
    content: [
      "./src/**/*.html",
      "./src/**/*.js",
      "./src/**/*.jsx",
      "./src/**/*.ts",
      "./src/**/*.tsx",
      "./public/index.html"
    ],
    // Options passed to PurgeCSS
    options: {
      // Whitelist specific selectors by name
      // whitelist: [],
    }
  }
};
