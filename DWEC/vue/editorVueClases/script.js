Vue.createApp({
    data() {
        return {
            red: false,
            blue: false,
            green: false,
            x2: false,
            x4: false,
            x6: false,
            bred: false,
            bblue: false,
            bgreen: false,
            texto: '',
            respuesta: ''
        }
    },
    methods: {
        inputRespuesta(){
            this.respuesta = this.texto
            this.texto = ''
        }
    }
}).mount('#app')  