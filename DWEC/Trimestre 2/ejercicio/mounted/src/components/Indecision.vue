<template>
    <section id="principal">
        <img v-if="imagen" :src="imagen">
        <div class="indecision-container">
            <input v-model="pregunta" type="text"
                placeholder="Pregunta de Si o No...">
            <div class="respuesta">
                <h1>{{ respuesta }}</h1>
            </div>
        </div>
    </section>
</template>

<script>
export default {
    name: 'indecisionApp',
    data() {
        return {
            pregunta: '',
            respuesta: null,
            imagen: null,
            cont : 0,
        }
    },
    methods: {
        async obtenerRespuesta() {
            this.respuesta = 'Pensando...'
            const apiKey = "https://yesno.wtf/api"
            const { answer, image } = await fetch(apiKey).then(res => res.json())
            this.respuesta = answer
            this.imagen = image
            return answer
        }
    },
    watch: {
        pregunta(valor) {
            if ( valor.endsWith('?') && this.cont == 0) {
                this.obtenerRespuesta()
                this.cont ++
            }
            if (valor.length == 0) {
                this.cont = 0
            }
        }
    }
}
</script>

<style>
#principal {
    display: flex;
    flex-direction: column;
    text-align: center;
}

input {
    height: 1.5rem;
    padding-left: 5px;
    margin-top: 1rem;
}
</style>