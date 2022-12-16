<template>
    <div>
        <input type="text" placeholder="Convertir Minusculas" v-model="pregunta">
        <h1>{{ respuesta }}</h1>
    </div>
</template>

<script>
export default {
    name: 'MinusculasVue',
    data() {
        return {
            respuesta: '',
            pregunta: ''
        }
    },
    watch: {
        pregunta(valor){
            if (valor.includes('.')) {
                this.obtenerRespuesta()
            }
        }
    },
    methods: {
        obtenerRespuesta(){
            const convertirMinusculas = this.pregunta.toLowerCase()
            this.respuesta = `Nº de minuscula ${convertirMinusculas}`
        }
    }
}
</script>

<style>

</style>
