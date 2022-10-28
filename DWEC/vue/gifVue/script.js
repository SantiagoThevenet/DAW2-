const vueapp = Vue.createApp({
    data() {
        return {
            array: [
                {
                    gif: 'https://acegif.com/wp-content/uploads/spanish-flag-14.gif',
                    pais: 'España'
                },
                {
                    gif: 'https://acegif.com/wp-content/uploads/gifs/france-flag-1.gif',
                    pais: 'Francia'
                },
                {
                    gif: 'https://upload.wikimedia.org/wikipedia/commons/1/10/Bandera_Colombia_Animacion.gif',
                    pais: 'Colombia'
                },
                {
                    gif: 'https://media.tenor.com/iEcw6FQcly4AAAAC/brasil-bandeira.gif',
                    pais: 'Brazil'
                },
                {
                    gif: 'https://i.pinimg.com/originals/de/d2/c3/ded2c345688d874af5b4fb170804eb82.gif',
                    pais: 'Argentina'
                }
            ],
            texto: '',
            correcto: '',
            numRan: Math.floor(Math.random() * 5),
        }
    },
    methods: {
        bandera(){
            
            if (this.texto == this.array[this.numRan].pais) {
                this.correcto = 'https://media.tenor.com/uvsw3p_srf8AAAAM/correcto-finn.gif'
            }else {
                this.correcto = 'http://comunidad.iebschool.com/iebs/files/2015/04/8-emociona-gente.gif'
            }
        },
        img() {
            return this.array[this.numRan].gif
        }
    }
}).mount('#app')
 
