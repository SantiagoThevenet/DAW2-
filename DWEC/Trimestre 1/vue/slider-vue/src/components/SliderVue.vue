<template>
  <section>
    <button @click="patras()">Atras</button>
    <img :src="lista[contador]">
    <button @click="palante()">Alante</button>
  </section>
</template>

<script>
export default {
    name: 'SliderVue',
    data() {
        return{
            lista:[
                'https://images.unsplash.com/photo-1553615738-d8e0829f1d61?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxleHBsb3JlLWZlZWR8M3x8fGVufDB8fHx8&w=1000&q=80',
                'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSMN8Mw5VWUvmUnb1CEGp1NFC9ua8jz9c-kkgQb3PLetPNaR7NbLcthmvDGpmoZ_Ruallo&usqp=CAU',
                'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSt7b-jONG2YN-pEybx4hJXGrr8n3sog_vzogqg64oYG9ZSoc8hfNCjWzdAGAizop9X5Z8&usqp=CAU'
            ],
            contador: 0,
            
        }
    }
}
</script>

<style>

</style>