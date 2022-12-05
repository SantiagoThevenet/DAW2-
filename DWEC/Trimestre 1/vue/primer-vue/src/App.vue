<template>
  <ListaCompraVue />
  <ListaCompraVue />
</template>

<script>
import ListaCompraVue from './components/ListaCompra.vue';

export default {
  name: 'App',
  components: {
    ListaCompraVue
  }
}
</script>
  
<style>
  * {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
    color: white;
  }
</style>
