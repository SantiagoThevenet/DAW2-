const fs = require('fs')
// // Las funciones de forma sincrona ejecutan las operaciones que hay dentro de estas y hasta que no acabe el proceso no seguira con las otras operaciones
// fs.writeFileSync('/data/six.txt', 'primera linea', {
//     flag: 'a'
// })


// Las funciones de forma asincrona permiten seguir ejecutando con otras operaciones miestras la funcion que hemos ejecutado esta terminando 
fs.writeFile('./data/six.txt', 'primera linea', {
    flag: 'a'}, (err) => {
        if (err) {
            console.log(err);
        } else {
            console.log('El archivo se ha creado');
        }
    }
)


console.log('ultima liena de codigo');