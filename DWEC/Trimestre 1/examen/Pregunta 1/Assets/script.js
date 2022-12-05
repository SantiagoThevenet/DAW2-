import miArray from "./datos.js"

const getData = () => {
    const body = document.body
    const main = document.createElement('main')
    body.appendChild(main)
    for (let i = 0; i < miArray.length; i++) {
        const { name } = miArray[i]
        const { email } = miArray[i]
        const { gender } = miArray[i]
        const { about } = miArray[i]
        const { friends } = miArray[i]

        const nameh1 = document.createElement('h1')
        nameh1.innerHTML = name
        const emailh2 = document.createElement('h2')
        emailh2.innerHTML = `<i class="fas fa-envelope-open-text"></i>${email}`
        const genderh2 = document.createElement('h2')
        genderh2.innerHTML = `<i class="fas fa-user"></i> ${gender}`
        const abouth2 = document.createElement('h2')
        abouth2.innerHTML = `<i class="far fa-address-card"></i>Acerca de ${name}`
        const aboutp = document.createElement('p')
        aboutp.innerHTML = about
        const firendsh2 = document.createElement('h2')
        firendsh2.innerHTML = `<i class="far fa-address-card"></i>Amistades de ${name}:`
        const firendsul = document.createElement('ul')
        for (let x = 0; x < friends.length; x++) {
            const firendsli = document.createElement('li')
            firendsli.textContent = friends[x].name
            firendsul.appendChild(firendsli)
        }
    
        const caja = document.createElement('div')
        caja.appendChild(nameh1)
        caja.appendChild(emailh2)
        caja.appendChild(genderh2)
        caja.appendChild(abouth2)
        caja.appendChild(aboutp)
        caja.appendChild(firendsh2)
        caja.appendChild(firendsul)

        main.appendChild(caja).setAttribute('class','caja')
    }
}
getData()