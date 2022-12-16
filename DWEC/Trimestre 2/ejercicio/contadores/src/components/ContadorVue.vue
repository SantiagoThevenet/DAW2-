<template>
    <div id="suu">
        <h1>{{(nombre || 'suuuuuuuuuuuu')}}</h1>
        <div id="id">
            <button @click="decrementer()" class="boton">-{{candidad}}</button>
            <h1 id="suh11">{{ contador }}</h1>
            <button @click="incrementar()" class="boton">+{{candidad}}</button>
        </div>
    </div>
</template>

<script>
export default {
    name: 'ContadorVue',
    props:{
        nombre: String,
        candidad: Number
    },
    data() {
        return {
            contador: 0
        }
    },
    methods: {
        incrementar() {
            this.contador = this.contador+Number(this.candidad)
        },
        decrementer() {
            this.contador = this.contador-Number(this.candidad)
        }
    }
}
</script>

<style>
#suh11{
    margin: 0 1rem;
}
#suu {
    border: 1px solid;
    margin: 3rem;
    width: 20%;
    height: 30vh;
    display: flex;
    justify-content: center;
    align-items: center;
    flex-direction: column;
}
#id {
    display: flex;
    flex-direction: row;
    justify-content: center;
    align-items: center;
}
button{
    cursor: pointer;
    background: none;
    border: 1px solid;
    border-radius: 5px;
    padding: .8rem 1.5rem;
}
</style>