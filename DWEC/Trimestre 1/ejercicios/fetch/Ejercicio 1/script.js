// Ejercicios 1
// const sumar = ( a, b ) => a + b
// console.log(sumar(2, 3))


// Ejercicio 2
// const contarOcurrencias = (palabra, letra) => {
//     let cont = 0
//     for (let i = 0; i < palabra.length; i++) {
//         if (letra === palabra[i]) {
//             cont++
//         }
//     }
//     return cont
// }

// console.log(contarOcurrencias("sarasa", "a")); // imprime 3
// console.log(contarOcurrencias("sarasa", "z")); // imprime 0


// Ejercicio 3
// const agregarIndice = (palabra) => {
//     let palabraN = '' 
//     for (let i = 0; i < palabra.length; i++) {
//         palabraN = palabraN+palabra[i]+i
//     }
//     return palabraN
// }

// console.log(agregarIndice("kawabonga")); // imprime "k0w1a2b3o4n5g6a7"
// console.log(agregarIndice("casa")); // imprime "c0a1s2a3"


// // Ejercicio 4
// const factura = {
//     numero: 1,
//     cliente: 'santiago',
//     divisa: 'EUR',
//     subtotal: 12,
//     iva: 21
// }

// const funcionFactura = (factura) => ({ numero, cliente, divisa, subtotal, iva } = factura)
// console.log(funcionFactura(factura));


console.log('santiago'.split())