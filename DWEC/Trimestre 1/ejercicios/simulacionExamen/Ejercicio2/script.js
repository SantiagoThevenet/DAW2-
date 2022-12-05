const apiKey = 'https://jsonplaceholder.typicode.com/users'

axios.get(apiKey).then(res => {
    const { data } = res
    console.log(data)

    
    const tabla = document.getElementById('tabla')
    for (let i = 0; i < data.length; i++) {
        const tr = document.createElement('tr')
        const tdNombre = document.createElement('td')
        const tdEmail = document.createElement('td')
        const tdCiudad = document.createElement('td')
        const tdCP = document.createElement('td')
        const tdCalle = document.createElement('td')
        tdNombre.textContent = data[i].name
        tdEmail.textContent = data[i].email
        tdCiudad.textContent = data[i].address.city
        tdCP.textContent = data[i].address.zipcode
        tdCalle.textContent = data[i].address.street


        tr.append(tdNombre)
        tr.append(tdEmail)
        tr.append(tdCiudad)
        tr.append(tdCP)
        tr.append(tdCalle)
        tabla.appendChild(tr)
    }
    
})
