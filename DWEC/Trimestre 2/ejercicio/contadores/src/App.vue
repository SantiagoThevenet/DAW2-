<template>
  <h1 id="suh1">Contador VUE <i class="fa-brands fa-linux"></i></h1>
  <div id="principal">
    <contador-vue nombre="X 1" candidad="1" />
    <contador-vue nombre="X 2" candidad="2" />
    <contador-vue nombre="X 3" candidad="3" />
    <contador-vue nombre="X 4" candidad="4" />
    <contador-vue nombre="X 5" candidad="5" />
    <contador-vue nombre="X 6" candidad="6" />
  </div>
</template>

<script>
import ContadorVue from './components/ContadorVue.vue'

export default {
  name: 'App',
  components: {
    ContadorVue

  }
}
</script>

<style>
#suh1 {
  margin-bottom: 2rem;
  font-size: 2.4rem;
}

#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}

#principal {
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
  align-items: center;

}
</style>
