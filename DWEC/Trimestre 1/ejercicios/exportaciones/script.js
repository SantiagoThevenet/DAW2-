import heroes from "./data/data.js";


const principal = document.getElementById('principal')

for (let i = 0; i < heroes.length; i++) {

    let div = document.createElement('div')

    let p = document.createElement('p')
    let h2 = document.createElement('h2')
    let img = document.createElement('img')
    let button = document.createElement('button')
    
    p.textContent = heroes[i].id
    h2.textContent = heroes[i].nombre
    img.src = heroes[i].img
    button.textContent = heroes[i].nombre
    
    
    principal.appendChild(div)

    div.appendChild(img)
    div.appendChild(h2)
    div.appendChild(p)
    div.appendChild(button)
}