Vue.createApp({
    data() {
        return {
            texto: '',
            respuesta: ''
        }
    },
    methods: {
        textoUser() {
            this.respuesta = this.texto
            this.texto = ''
        },
        size(num) {
            const h1 = document.getElementById('h1Respuesta')
            h1.style.fontSize = num + 'rem'
        },
        color(color) {
            const h1 = document.getElementById('h1Respuesta')
            h1.style.color = '#' + color
        },
        background(color) {
            const h1 = document.getElementById('h1Respuesta')
            h1.style.background = '#' + color
        }
    }
}).mount('#app')