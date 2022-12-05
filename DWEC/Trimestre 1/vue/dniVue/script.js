Vue.createApp({
    data(){
        return {
            numero: '',
            responseL: '',
            response: ''
        }
    },
    methods: {
        click(){
            const arrayDNI = ["T", "R", "W", "A", "G", "M", "Y", "F", "P", "D", "X", "B", "N", "J", "Z", "S", "Q", "V", "H", "L", "C", "K", "E"] 
            const num = this.numero%23
            if (this.numero.toString().length == 8) {
                this.response = this.numero+arrayDNI[num]
                this.responseL = arrayDNI[num]
            }else{
                this.response = "Debe tener 8 digitos"
            }
        }
    }
}).mount('#app')

