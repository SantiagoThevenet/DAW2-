<template>
  <FormularioDatosVue />
</template>

<script>
import FormularioDatosVue from './components/FormularioDatos.vue';
export default {
  name: 'App',
  components: {
    FormularioDatosVue
  }
}
</script>

<style>
*{
  margin: 0;
  padding: 0;
  box-sizing: border-box;
  font-family: 'Comfortaa', cursive;

}

body{
  display: flex;
  align-items: center;
  justify-content: center;
  height: 100vh;
}
@media only screen and (max-width: 762px) {
  body{
    height: 140vh;
  }
}
</style>
