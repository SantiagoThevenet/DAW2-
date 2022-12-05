<template>
    <div id="main">
        <div id="mayores">
            <h1>Mayores de edad</h1>
            <h4 v-for="i in almacenar" :key="i.nombre"><span v-if="(i.edad >= 18)">{{ i.nombre }}</span></h4>
        </div>

        <div id="menores">
            <h1>Menores de edad</h1>
            <h4 v-for="i in almacenar" :key="i.nombre"><span v-if="(i.edad <= 18)">{{ i.nombre }}</span></h4>
        </div>
    </div>
</template>

<script>
export default {
    name: 'resultadoDatos',
    props: {
        nombre: String,
        edad: Number,
        almacenar: Array
    }
}
</script>

<style>
#main{
    display: flex;
    align-items: center;
    justify-content: center;
}
#mayores,#menores{
    border: 1px solid;
    padding: 1rem;
    margin: 1rem;
    border-radius: 1rem;
    height: 60vh;
    width: 50vh;
    display: flex;
    align-items: center;
    flex-direction: column;
    box-shadow: -3px 3px 3px black;
}
h1{
    margin-top: 1rem;
}
h4{
    margin: .2rem;
}

@media only screen and (max-width: 762px) {
    #main{
        flex-direction: column;
    }
    #mayores,#menores{
        height: 50vh;
        width: 40vh;
    }
}
</style>


