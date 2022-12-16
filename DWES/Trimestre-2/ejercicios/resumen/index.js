console.log('HOLA MUNDO')


//Inicializar proyectos 
// npm init


// Si nuestra version de paquete actual es 1.0.0
// ^ => Actualiza hasta antes de la version 1.1.0 
// ~ => Actualiza hasta antes de la verison 2.0.0

// En el package.json => script, si añadimos "start": "node index.js" nos permite ejecutar nuestro script con solo npm start


// Borrar modulo
// npm remove nodemon


// NODEMON ==> nodemon equivale a liveserver
// npm i nodemon -D
// El -D añade nodemon a devDependencies, eso son los modulos que se usan en el desarollo pero no son 
// relevantes en el funcionamiento del programa 


// NPX ==> Siver para ejeuctar un modulo pero sin descargarlo


// const fs = require('fs')
// // Las funciones de forma sincrona ejecutan las operaciones que hay dentro de estas y hasta que no acabe el proceso no seguira con las otras operaciones
// fs.writeFileSync('/data/six.txt', 'primera linea', {
//     flag: 'a'
// })


// // Las funciones de forma asincrona permiten seguir ejecutando con otras operaciones miestras la funcion que hemos ejecutado esta terminando 
// fs.writeFile('./data/six.txt', 'primera linea', {
//     flag: 'a'}, (err) => {
//         if (err) {
//             console.log(err);
//         } else {
//             console.log('El archivo se ha creado');
//         }
//     }
// )


// console.log('ultima liena de codigo');