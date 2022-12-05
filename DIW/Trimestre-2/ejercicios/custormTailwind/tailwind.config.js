/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./public/index.html"],
  theme: {
    extend: {
      fontFamily: {
        comfortaa: "'Comfortaa', cursive"
      },
      colors:{
        'santi':'#123456'
      },
      padding: {
        'chechu': '10rem'
      },
      height: {
        '80vh' : '80vh'
      }
    },
  },
  plugins: [],
}
