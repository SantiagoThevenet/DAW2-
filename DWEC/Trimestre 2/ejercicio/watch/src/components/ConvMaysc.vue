<template>
    <div>
        <input type="text" placeholder="Convertir Mayusculas" v-model="pregunta">
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
            const convertirMayusculas = this.pregunta.toUpperCase()
            this.respuesta = `Nº de minuscula ${convertirMayusculas}`
        }
    }
}
</script>

<style>

</style>
