<template>
  <div id="main">
        <h1>Comparador de Números</h1>
        <div class="inputs">
            <input placeholder="Número" type="number" id="input1" v-model="num1">
            <input placeholder="Número" type="number" id="input2" v-model="num2">
        </div>
        <button @click="comparar()">Coparar</button>
        <p>{{ parrafo }}</p>
    </div>
</template>

<script>
export default {
    name: 'ComparadorVue',
    data() {
        return {
            num1: 0,
            num2: 0,
            parrafo: ''
        }
    },
    methods: {
        comparar() {
            if ( Number(this.num1) > Number(this.num2) ){
                this.parrafo = `${this.num1} es mayor que ${this.num2}`
            }else if (Number(this.num1) < Number(this.num2) ) {
                this.parrafo = `${this.num1} es menor que ${this.num2}`
            }else{
                this.parrafo = `${this.num1} es igual que ${this.num2}`
            }
        }
    }
}
</script>

<style>

</style>