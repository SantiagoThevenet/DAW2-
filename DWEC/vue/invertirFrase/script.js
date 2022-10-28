// Crea una aplicación en vue que permita al usuario escribir una  frase y creando un método de vue
// se debe invertir la cadena y mostrarla en la interfaz al pulsar la tecla enter, haciendo uso de v-on:keyup.enter.



Vue.createApp({
    data() {
        return {
            texto: '',
            resultado:''
        }
    },
    methods: {
        invertirTexto() {
            this.resultado = this.texto.split("").reverse().join("");
        }
    }
}).mount('#app')