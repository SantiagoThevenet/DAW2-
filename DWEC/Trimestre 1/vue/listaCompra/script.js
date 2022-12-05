const mi_app = Vue.createApp({
    data() {
        return {
            titulo: "Lista de la compra",
            texto: "",
            edit:false,
            lista:[],
            imagen: 'http://2.bp.blogspot.com/-JRjd1cIWE0k/UE4k8lDMbrI/AAAAAAAAAXA/XHBBh1Fi2rY/s1600/gato+gordo.jpg'
        }
    },
    methods:{
        guardarElemento(){
            this.lista.push(this.texto)
            this.texto = ''
        },
        borrarElemento(){
            this.lista.pop()
        },
        editando(a){
            this.edit = a
        }
    }
}).mount("#mi_app");
