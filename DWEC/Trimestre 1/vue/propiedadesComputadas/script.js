Vue.createApp({
    data() {
        return {
            caracteres: '',
        }
    },
    computed: {
        logitud() {
            return this.caracteres.length
        },
        nCharEsp(){
            return this.caracteres.split(' ').join('').length
        },
        nPal(){
            let pal = this.caracteres.split(' ')
            let cont = 0
            for (let i = 0; i < pal.length; i++) {
                if (pal[i] != '') {
                    cont++
                }
            }
            return cont

        },
        nEsp(){
            let frase = this.caracteres
            frase = frase.split(' ')
    
            return frase.length-1
        },
        primPalabra(){
            let frase = this.caracteres
            frase = frase.split(' ')
            return frase[0]

        },
        ultPalabra(){
            let pal = this.caracteres.split(' ')
            let cont = 0
            for (let i = 0; i < pal.length; i++) {
                if (pal[i] != '') {
                    cont = i
                }
            }
            return pal[cont]
        }
    }
}).mount('#mi_app')