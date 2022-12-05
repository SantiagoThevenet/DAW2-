<template>
    <section id="principal">
        <div id="mi_app">
            <header>
                <h1>{{ titulo || 'Bienvenido' }}</h1>
                <button v-if="edit" @click="editando(false)">Cancelar</button>
                <button v-else @click="editando(true)">Añadir elemento</button>
            </header>
            <div v-if="edit">
                <input placeholder="Producto: " type="text" @keyup.enter="guardarElemento" v-model="texto">
                <div>
                    <button @click="guardarElemento">Añadir</button>
                    <button v-if="lista.length >= 1" @click="borrarElemento">Borrar</button>
                </div>

                <ul>
                    <li :class="{ tachado: elemento.tachado == true }" v-for="elemento in listaOrdenada"
                        :key="elemento.futa" @click="tachado(elemento)">{{ elemento.fruta }}</li>
                </ul>
                <p v-if="lista.length === 0">No hay elemento en la lista</p>
            </div>
        </div>
    </section>
</template>

<script>
export default {
    name: 'listaCompra',
    data() {
        return {
            titulo: 'Lista de la compra',
            texto: '',
            edit: false,
            lista: [
                {
                    fruta: 'Kiwi',
                    tachado: true
                }
            ]
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
    }
}
</script>

<style>

body {
    width: 100%;
    background: #ff0e0e;
    background: linear-gradient(90deg, #cf4343 0%, #cfd139 100%);
    display: flex;
    align-items: center;
    justify-content: center;
    height: 100vh;
}

body section {
    width: 100%;
}

body section #mi_app {
    background: #000000;
    border-radius: 5px;
    box-shadow: 5px 5px 5px #fffbfb;
}

body section #mi_app header {
    width: 100%;
    display: flex;
    justify-content: center;
    flex-direction: row;
    align-items: center;
}

body section #mi_app header button {
    width: 10rem;
    height: 2rem;
    margin: 2rem;
    background: none;
    border: 1px solid;
    border-radius: 5px;
}

body section #mi_app div {
    width: 100%;
    display: flex;
    align-items: center;
    justify-content: center;
    flex-direction: column;
}

body section #mi_app div div {
    display: flex;
    flex-direction: column;
}

body section #mi_app div div button {
    width: 10rem;
    height: 2rem;
    margin: 1rem 0.5rem;
    background: none;
    border: 1px solid;
    border-radius: 5px;
}

body section #mi_app div input {
    padding-left: 5px;
    margin: 1rem;
    width: 50%;
    height: 2rem;
    color: black;
}

body section #mi_app div input::-moz-placeholder {
    color: black;
}

body section #mi_app div input:-ms-input-placeholder {
    color: black;
}

body section #mi_app div input::placeholder {
    color: black;
}

body section #mi_app div ul {
    max-height: 40vh;
    overflow-y: scroll;
    margin: 5rem 0;
}

body section #mi_app div ul li {
    list-style: none;
    margin: 1rem;
}

body section #mi_app div p {
    margin: 1rem;
}

.tachado {
    text-decoration: line-through;
}

/*# sourceMappingURL=style.css.map */
</style>