
let cosa = Vue.createApp({
    data() {
        return {
            texto: '',
            mi_array: []
        }
    },
    methods:{
        guardarElemento(){
            this.mi_array.push(this.texto)
        }
    }

})
.mount('#mi_app')
