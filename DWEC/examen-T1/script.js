// Ojetos literales
// const persona = {
//     nombre: 'Santiago',
//     apellido: 'Thevenet',
//     direccion: {   
//         ciudad: 'Valencia',
//         nacionalidad: 'España'
//     }
// }

// // const personaCopia = persona //Copiando de esta forma los cambios que hagamos despues se actualizaran en los dos objetos
// const personaCopia = {...persona}  //Asi no se guardaran los cabios en los dos objetos
// personaCopia.apellido = 'Soler'
// console.log(persona)

// console.log(personaCopia)


const miArry = [
    {
        id: 1,
        nombre: 'pepe'
    },
    {
        id: 1,
        nombre: 'santi'
    },
    {
        id: 2,
        nombre: 'santi'
    }
]

// Find: Devuelve el valor del primer elemento del array que cumple la función de prueba proporcionada.
const findarray = miArry.find(i => i.id == 1)
// Filter: Crea un nuevo array con todos los elementos que cumplan con la condición implementada por la función dada
const filterarray = miArry.find(i => i.nombre == 'santi')

console.log(findarray);
console.log(filterarray);
// Desesctucturacion
// Importacion Exportacion
// Promesas
// Fetch 
// Axios
// Async/Await
// Ternarios/check null