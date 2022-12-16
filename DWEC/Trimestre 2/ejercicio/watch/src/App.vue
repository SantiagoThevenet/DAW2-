<template>
  <MinusculasVue />
  <MayusculasVue />
  <ConvMaysc />
  <ConvMinus />
  <EspaciosBlanco />
</template>

<script>
import MinusculasVue from './components/Minusculas.vue';
import MayusculasVue from './components/Mayusculas.vue';
import ConvMaysc from './components/ConvMaysc';
import ConvMinus from './components/ConvMinus';
import EspaciosBlanco from './components/EspBlanco.vue';
export default {
  name: 'App',
  components: {
    MinusculasVue,
    MayusculasVue,
    ConvMaysc,
    ConvMinus,
    EspaciosBlanco

  }
}
</script>

<style>
body{
  display: flex;
  align-items: center;
  justify-content: center;
  flex-direction: column;
  height: 100vh;
}
#app{
  background-color: brown;
  box-shadow: 5px 5px 5px rgb(129, 122, 122);
}
div{
  margin: 1rem;
  padding: 1rem;
  border-radius: 5px;
}

input{
  height: 2rem;
  padding-left: 5px;
  width: 40rem;
  box-shadow: 5px 5px 5px black;
  border: none;
  border-radius: 5px;
}
h1{
  font-size: 16px;
}
</style>
