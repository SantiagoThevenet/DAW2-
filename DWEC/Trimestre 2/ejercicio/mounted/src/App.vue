<template>
  <Indecision/>
</template>

<script>
import Indecision from './components/Indecision.vue';


export default {
  name: 'App',
  components: {
    Indecision
}
}
</script>

<style>
body{
  font-family: 'Rubik', sans-serif;
  background-color: rgb(0, 0, 0); 
  display: flex;
  align-items: center;
  justify-content: center;
  height: 100vh;
  color: white;
}
img{
  width: 30rem;
  height: 30rem;
  border-radius: 10px;
  box-shadow: 10px 10px 10px white;
}

</style>
