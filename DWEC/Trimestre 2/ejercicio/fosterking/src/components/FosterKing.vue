<template>
    <section id="principal">
        <div id="titulo">
            <h1>FosterKing</h1>
            <p>Lorem ipsum dolor, sit amet consectetur adipisicing elit. Modi explicabo assumenda numquam obcaecati?
                Necessitatibus dicta placeat, aspernatur exercitationem quidem mollitia facere eligendi laborum sequi
                enim eveniet veritatis repellendus laudantium quae!</p>
        </div>
        <div id="caja-menu">
            <div id="muestra">
                <div id="caja-img">
                    <img :src="imagen">
                </div>
                <h3>{{ plato || 'La mejor comida basura de Valencia' }}</h3>
                <p>Lorem ipsum dolor sit, amet consectetur adipisicing elit. Officiis est distinctio, praesentium sint
                    laudantium ipsam alias corrupti unde dolores rerum placeat adipisci numquam magni a maiores iste
                    veniam! Aspernatur, culpa?</p>
            </div>
            <div id="menu">
                <h2>Nuestro Menú</h2>
                <ul>
                    <li v-for="producto in productos" :key="producto.id" @click="mostrarProducto(producto.nombre)">
                        {{ producto.nombre }}</li>
                </ul>
                <div id="formulario">
                    <input type="text" placeholder="Nombre plato" v-model="inputText">
                    <input type="url" placeholder="Url de la imagen" v-model="inputUrl">
                    <input type="button" value="Insertar" id="boton" @click="insertarPlato()">
                </div>
            </div>
        </div>
    </section>
</template>

<script>
export default {
    name: 'FosterKing',
    data() {
        return {
            imagen: 'https://wallpaperaccess.com/full/3014596.jpg',
            plato: '',
            inputText: '',
            inputUrl: '',
            cont: 4,
            productos: [
                {
                    id: 0,
                    nombre: 'Ensalada Cesar',
                    imagen: 'https://static-sevilla.abc.es/media/gurmesevilla/2010/02/ensalada-cesar-receta.jpg'
                },
                {
                    id: 1,
                    nombre: 'Big King Huevo',
                    imagen: 'https://fondosmil.com/fondo/75572.jpg'
                },
                {
                    id: 2,
                    nombre: 'Costillas BBQ',
                    imagen: 'https://recetasoster.com/wp-content/uploads/2020/05/Costillitas-con-salsa-bbq-de-winky-y-cafe.jpg'
                },
                {
                    id: 3,
                    nombre: 'Pizza',
                    imagen: 'https://images8.alphacoders.com/644/thumb-1920-644361.jpg'
                },
                {
                    id: 4,
                    nombre: 'Quesallida de Pollo',
                    imagen: 'https://truffle-assets.imgix.net/1t1bxm43v4e3_1IO7h5BvQsK6UiEaOcQSUQ_quesadillas-de-pollo_landscapeThumbnail_es.jpeg'
                },
            ],
        }
    },
    methods: {
        mostrarProducto(x) {
            let buscador = this.productos.find(i => i.nombre == x)
            this.imagen = buscador.imagen
            this.plato = buscador.nombre
        },
        insertarPlato() {
            this.cont++
            this.productos.push({
                id: this.cont,
                nombre: this.inputText,
                imagen: this.inputUrl
            }) 
            this.inputText = ''
            this.inputUrl = ''
        }
    }
}
</script>

<style>
    #principal {
        padding: 0 10rem;
        display: flex;
        justify-content: center;
        align-items: center;
        flex-direction: column;
        height: 100vh;
    }

    #principal #caja-menu {
        padding: 1rem;
        display: flex;
        justify-content: space-between;
        background: #ffffffdb;
    }

    #titulo {
        text-align: center;
        background: #ffffffdb;
        padding: 1rem;
    }

    #titulo h1 {
        font-size: 40px;
    }

    #titulo p {
        margin: 1rem;
        color: gray;
    }

    #caja-menu #muestra {
        width: 50%;
        padding: 1rem;
        display: flex;
        flex-direction: column;
        justify-content: space-between;
    }
    #muestra #caja-img{
        width: 100%;
        display: flex;
        justify-content: center;
        align-items: center;
    }
    #muestra h3{
        font-size: 20px;
        margin: 1rem 0;
    }
    #muestra p{
        font-weight: 300;
    }
    #caja-menu #muestra img{    
        width: 100%;
        border-radius: 10px;
        box-shadow: 2px 2px 5px  black;
    }
    #menu{
        width: 35%;
        padding: 1rem;
        display: flex;
        justify-content: start;
        flex-direction: column;
    }
    #menu ul {
        list-style: none;
        overflow-y: scroll;
        height: 15rem;
    }
    #menu ul li {
        cursor: pointer;
        font-size: 18px;
        margin: 1rem 1rem 1rem 0;
        font-weight: 300;
    }
    #menu ul li:hover{
        text-decoration: underline;
    }

    #formulario{
        display: flex;
        flex-direction: column;
    }
    #formulario input{
        padding: .8rem 1rem;
        margin:  .5rem .5rem .5rem 0;
        outline: none;
    }
    #boton{
        width: 8rem;
        cursor: pointer;
        border: none;
        background: #123456;
        color: white;
        border-radius: 10px;
    }
    
    @media only screen and (max-width: 768px) {
        #principal{
            height: inherit;
            padding: 1rem;
        }
        #principal #caja-menu{
            flex-direction: column;
        }
        #muestra, #menu{
            width: 100% !important;
        }
    }
</style>