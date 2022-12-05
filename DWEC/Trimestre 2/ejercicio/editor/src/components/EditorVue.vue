<template>
    <div id="main">
        <h1>Editor con Vue</h1>
        <div id="caja-edicion">
            <div id="imagen">
                <img :src="listaImg[imgRandom]" :style="{ filter: `contrast(${rangoContraste}) saturate(${rangoSaturacion}) brightness(${rangoBrillo}) blur(${rangoDesenfoque}px)`}">
            </div>
        </div>
        <div id="edit">
            <div>
                <h3>Contraste {{rangoContraste}}%</h3>
                <input type="range" min="0" max="10" step="0.01" v-model="rangoContraste">
            </div>
            <div>
                <h3>Saturacion {{rangoSaturacion}}%</h3>
                <input type="range" min="0" max="10" step="0.01" v-model="rangoSaturacion">
            </div>
            <div>
                <h3>Brillo {{rangoBrillo}}%</h3>
                <input type="range" min="0" max="10" step="0.01" v-model="rangoBrillo">
            </div>
            <div>
                <h3>Desenfoque {{rangoDesenfoque}}%</h3>
                <input type="range" min="0" max="10" step="0.01" v-model="rangoDesenfoque">
            </div>
        </div>
    </div>
</template>

<script>
export default {
    name: 'EditorVue',
    data() {
        return {
            rangoContraste: 1,
            rangoSaturacion: 1,
            rangoBrillo: 1,
            rangoDesenfoque: 1,
            listaImg: ['https://ih1.redbubble.net/image.2695997250.5815/fposter,small,wall_texture,product,750x1000.jpg','https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcREvLt4XdWHAaAV38NEuQOR71-YvWVZLnS5DA&usqp=CAU','https://lwlies.com/wp-content/uploads/2021/05/shrek-pond-fart.jpg'],
            imgRandom: Math.floor(Math.random()*3)
        }
    }
}
</script>

<style>
    #main {
        display: flex;
        justify-content: center;
        align-items: center;
        flex-direction: column;
        height: 100vh;
    }

    h1{
        font-size: 40px;
    }
    #caja-edicion{
        display: flex;
        justify-content: space-around;
        align-items: center;
        flex-direction: column;
        width: 80%;
    }
    #imagen {
        width: 66%;
        display: flex;
        justify-content: center;
        align-items: center;
        padding: 1rem;
    }
    #imagen img { width: 30rem; height: 30rem; }
    #edit {
        width: 90%;
        display: flex;
        justify-content: space-around;

    }

    #edit div {
        width: 20%;
    }
    #edit div input {
        width: 100%;
    }
    h3{
        font-size: 1rem;
    }

    @media only screen and (max-width: 768px) {
        #caja-edicion{width: 100%;}
        #imagen img{width: 100%;}
        #edit{flex-direction: column;}
        #edit div{
            width: 100%;
            margin: .7rem 0;
        }
    }
</style>