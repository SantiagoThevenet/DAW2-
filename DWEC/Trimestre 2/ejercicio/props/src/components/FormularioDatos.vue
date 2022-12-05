<template>
    <div id="main2">
        <h1 id="h1">Propra con Vue</h1>
        <p>En este ejercicio se preactican las rops dinamicas de Vue</p>
        <div id="formulario">
            <input type="text" placeholder="Nombre" v-model="nombre">
            <input type="number" placeholder="Edad" v-model="edad">
            <button @click="guardar()">Guardar</button>
        </div>
    </div>
    <ResultadoDatosVue :nombre="nombre" :edad="edad" :almacenar="datos" />
</template>

<script>
import ResultadoDatosVue from './ResultadoDatos.vue';
export default {
    nombre: 'formularioDatos',
    data() {
        return {
            nombre: '',
            edad: 0,
            datos: []
        }
    },
    components: {
        ResultadoDatosVue
    },
    methods: {
        guardar() {
            this.datos.push({ nombre: this.nombre, edad: this.edad })
        }
    }
}
</script>

<style>
#h1 {
    font-size: 3rem;
    font-weight: 700;
}

#main2 {
    display: flex;
    justify-content: center;
    align-items: center;
    flex-direction: column;
    margin-bottom: 2rem;
    line-height: 3rem;
}

input {
    margin: 0 1rem;
    height: 2rem;
    padding-left: 5px;
}

button {
    background: none;
    border: 1px solid;
    border-radius: 5px;
    padding: .5rem 1rem;
    transition: .4s;
}

button:hover {
    background: brown;
    color: white;
}


@media only screen and (max-width: 762px) {
    #h1 {
        font-size: 2rem;
    }
    #formulario{
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
    }
    p{
        font-size: .8rem;
    }
    input{
        width: 100%;
        margin: .5rem 0;
    }
}
</style>