<template>
    <div>
        <input type="text" placeholder="Mayusculas" v-model="pregunta">
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
            const preguntaUpper = this.pregunta.toUpperCase()
            let cont = 0
            for (let i = 0; i < this.pregunta.length; i++) {
                if (this.pregunta[i] == preguntaUpper[i]) {
                    cont++
                }
            }
            this.respuesta = `Nº de mayusculas ${cont-1}`
        }
    }
}
</script>

<style>

</style>
