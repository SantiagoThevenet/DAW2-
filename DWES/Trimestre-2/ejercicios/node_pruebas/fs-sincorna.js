const fs = require('fs')

// const first = fs.readFileSync('./data/first.txt','utf-8')

// console.log(first);
// console.log(second.toString());


// fs.writeFileSync('./data/third.txt', 'esto es un tercer archivo')

// const title = '\nesto es un cuarto archivo'

// fs.writeFileSync('./data/four.txt',title, {
//     flag: 'a',
// })


fs.readFile('./data/first.txt', 'utf-8', (error, data) => {
    if (error) {
        console.log(error)
    } else {
        console.log(data)
    }
})

fs.readFile('./data/second.txt', 'utf-8', (error, data) => {
    if (error) {
        console.log(error)
    } else {
        console.log(data)
    }

    fs.writeFile('./data/newfile.txt', 'esto es un archivo nuevo desde fs', (error, data) => {
        console.log(error);
        console.log(data);
    })
})
