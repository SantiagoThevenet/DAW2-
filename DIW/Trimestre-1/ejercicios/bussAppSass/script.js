let inicio = document.getElementById('inicio')
let contact = document.getElementById('contact')
let carritoC = document.getElementById('carritoC')
carritoC.style.position = 'absolute'
carritoC.style.visibility = 'hidden'

const carrito = () => {

    carritoC.style.position = 'relative'
    carritoC.style.visibility = 'visible'

    inicio.style.position = 'absolute'
    inicio.style.visibility = 'hidden'
    contact.style.position = 'absolute'
    contact.style.visibility = 'hidden'

}
const quitarCarrito = () => {
    inicio.style.position = 'relative'
    inicio.style.visibility = 'visible'
    contact.style.position = 'relative'
    contact.style.visibility = 'visible'
    carritoC.style.position = 'absolute'
    carritoC.style.visibility = 'hidden'
}