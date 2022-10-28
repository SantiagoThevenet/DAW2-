const enviar = () => {
    const angulo1 = document.getElementById('angulo1').value
    const angulo2 = document.getElementById('angulo2').value
    const angulo3 = document.getElementById('angulo3').value
    
    const alerta = (angulo1 == angulo3 && angulo1 == angulo2) ? 'Equilatero' : 'Isoceles'

    const h1 = document.getElementById('h1')
    h1.textContent = alerta

    const su = document.getElementById('su')

    su.appendChild(h1)
}