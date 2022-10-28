let cosa = Vue.createApp({
    data() {
        return {
            numero: '',
            resultado: ''
        }
    },
    methods:{
        comprobar(){
            this.numero % 2 == 0 ? this.resultado = 'Par' : this.resultado = 'Inpar'
        }
    }

})
.mount('#mi_app')
