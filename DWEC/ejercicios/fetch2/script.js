const api = "https://randomuser.me/api/"

fetch(api)
    .then(res => res.json()
        .then(response => {
            const {results} = response
            const res = results[0]

            const nombre = document.getElementById('nombre')
            const email = document.getElementById('email')
            const tel = document.getElementById('tel')
            const pais = document.getElementById('pais')
            const ciudad = document.getElementById('ciudad')
            const img = document.getElementById('img')

            img.src =res.picture.large
            nombre.textContent = 'Nombre: '+res.name.first
            email.textContent = 'Email: '+res.email
            tel.textContent = 'Telefono: '+res.phone
            pais.textContent = 'Pais: '+res.location.country
            ciudad.textContent = 'Ciudad: '+res.location.city
            console.log(res);
        }))

const button = document.getElementById('button')
button.setAttribute('onclick', 'location.reload()')
