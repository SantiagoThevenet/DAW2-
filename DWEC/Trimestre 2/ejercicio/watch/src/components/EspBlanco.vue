<template>
    <div>
        <input type="text" placeholder="Espacios Blanco" v-model="pregunta">
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
            let cont = 0
            for (let i = 0; i < this.pregunta.length; i++) {
                if (this.pregunta[i] == ' ') {
                    cont++
                }
            }
            this.respuesta = `Espacios en blanco: ${cont}`
        }
    }
}
</script>

<style>

</style>
