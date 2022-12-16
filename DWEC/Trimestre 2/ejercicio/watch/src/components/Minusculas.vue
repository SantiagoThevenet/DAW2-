<template>
    <div>
        <input type="text" placeholder="Minusculas" v-model="pregunta">
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
            const preguntaLower = this.pregunta.toLowerCase()
            let cont = 0
            for (let i = 0; i < this.pregunta.length; i++) {
                if (this.pregunta[i] == preguntaLower[i]) {
                    cont++
                }
            }
            this.respuesta = `Nº de minuscula ${cont-1}`
        }
    }
}
</script>

<style>

</style>
