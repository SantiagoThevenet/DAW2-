const miArray = []
const cont1 =0
const cont2 =0
const buscar = () => {
    const buscardor = document.getElementById('buscardor').value
    const buscar = document.getElementById('buscar')
    const listaFilter = miArray.filter(i => buscardor == i.nombre || buscardor == i.apellido || buscardor == i.number)
    const div = document.getElementById('div1')
    div.innerHTML = " "
    console.log(listaFilter);
    if (listaFilter.length > 0) {
        for (let i = 0; i < listaFilter.length; i++) {
            const ul = document.createElement('ul')

            const nombreli = document.createElement('li')
            const apellidoli = document.createElement('li')
            const numberli = document.createElement('li')
     
            nombreli.innerHTML = `<b>Nombre</b>: ${listaFilter[i].nombre}`
            ul.appendChild(nombreli)
            apellidoli.innerHTML = `<b>Apellido</b>: ${listaFilter[i].apellido}`
            ul.appendChild(apellidoli)
            numberli.innerHTML = `<b>Number</b>: ${listaFilter[i].number}`
            ul.appendChild(numberli)
            div.appendChild(ul)

        }
        buscar.appendChild(div)
    }
}
const insertar = () => {
    var nombre = document.getElementById('nombre').value
    var apellido = document.getElementById('apellido').value
    var number = document.getElementById('number').value

    miArray.push({
        'nombre': nombre,
        'apellido': apellido,
        'number': number  
    })

    nombre = " "
    apellido = " "
    number = " "
}


const datos = () => {
    const datos = document.getElementById('datos')
    const div = document.createElement('div')
    div.innerHTML = ''
    if (miArray.length > 0) {
        for (let i = 0; i < miArray.length; i++) {
            const ul = document.createElement('ul')
            const nombreli = document.createElement('li')
            const apellidoli = document.createElement('li')
            const numberli = document.createElement('li')
    
            nombreli.innerHTML = `<b>Nombre</b>: ${miArray[i].nombre}`
            ul.appendChild(nombreli)
            apellidoli.innerHTML = `<b>Apellido</b>: ${miArray[i].apellido}`
            ul.appendChild(apellidoli)
            numberli.innerHTML = `<b>Number</b>: ${miArray[i].number}`
            ul.appendChild(numberli)

            div.appendChild(ul)
        }
        datos.appendChild(div)
    }
}

