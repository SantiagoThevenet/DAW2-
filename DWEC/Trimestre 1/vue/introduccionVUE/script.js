Vue.createApp({
    data() {
        return {
            nombre: '',
            apellido: '',
            fecha: '',
            opccion: '',
            mensaje: '' ,
        }
    }
}).mount('#fomulario')

const resultado = document.getElementById('resultado')
resultado.style.position = 'absolute'

const formulario = () => {
    const main = document.getElementById('formulario')
    main.style.visibility = 'hidden'
    main.style.position = 'absolute'
    
    const resultado = document.getElementById('resultado')
    resultado.style.visibility = 'visible'
    
    resultado.style.position = 'relative'

}

const enviar = () => {
    const main = document.getElementById('formulario')
    main.style.visibility = 'visible'
    main.style.position = 'relative'
    const resultado = document.getElementById('resultado')
    resultado.style.visibility = 'hidden'
    resultado.style.position = 'absolute'

}
