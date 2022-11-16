const mi_app = Vue.createApp({
    data() {
        return {
            titulo: "Lista de la compra",
            texto: "",
            edit: false,
            lista: [
                { fruta: 'kiwi', tachado: true }
            ],
            imagen: 'http://2.bp.blogspot.com/-JRjd1cIWE0k/UE4k8lDMbrI/AAAAAAAAAXA/XHBBh1Fi2rY/s1600/gato+gordo.jpg'
        }
    },
    computed: {
        listaOrdenada() {
            return [...this.lista].reverse()
        }
    },
    methods: {
        guardarElemento() {
            this.lista.push({ fruta: this.texto, tachado: false })
            this.texto = ''
        },
        borrarElemento() {
            this.lista.pop()
        },
        editando(a) {
            this.edit = a
        },
        tachado(elemento) {
            elemento.tachado = !(elemento.tachado)
        }
    },
}).mount("#mi_app");
