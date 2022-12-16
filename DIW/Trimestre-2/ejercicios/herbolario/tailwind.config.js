/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ['./index.html'],
  theme: {
    colors: {
      color1: '#07892F',
      color2: '#FCDD09',
      color3: '#DA131A'
    },
    screens:{
      'pc':'768px'
    },
    height:{
      'img': '60vh'
    },
    backgroundImage: {
      'gangaImg': "url('/img/hqdefault.jpg')",
    },
  },
  plugins: [],
}
