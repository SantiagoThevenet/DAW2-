// let p = new Promise((resolve, reject) => {
//     let a = 1 + 1;
//     if (a === 2) {
//         setTimeout( () => {
//             resolve("Exito");
//         },2000)

//     } else {
//         setTimeout( () => {
//             reject("Fracaso");
//         },1000)
//     }
// });



// p.then((mensaje) => {
//     console.log(mensaje);
// }).catch((mensaje) => {
//     console.log(mensaje);
// });


let objeto = [
    {
        nombre: 'cr7',
        imagen: 'https://www.realmadrid.com/img/vertical_380px/cristiano_550x650_20180917025046.jpg'
    },
    {
        nombre: 'gato',
        imagen: 'https://upload.wikimedia.org/wikipedia/commons/2/24/Stray_calico_cat_near_Sagami_River-01.jpg'
    },
    {
        nombre: 'perro',
        imagen: 'https://www.hola.com/imagenes/mascotas/20220615211797/razas-de-perro-elegantes/1-101-495/razas-de-perro-elegantes-m.jpg'
    },
    {
        nombre: 'mamut',
        imagen: 'https://static01.nyt.com/images/2021/09/13/science/15SCI-mammot-ESP-2/merlin_194444403_07111d04-29f0-4166-b510-aa3105c739c2-superJumbo.jpg?quality=75&auto=webp'
    }
]

let ranNum = Math.floor(Math.random()*(4 - 0)+0)


let img = document.getElementById('img')
img.src = objeto[ranNum].imagen

let body = document.getElementById('body')



let boton = () =>{
    let p = new Promise((resolve, reject) => {
        let input = document.getElementById('input').value
        let h2 = document.createElement('h2')

        if (input == objeto[ranNum].nombre) {
            resolve(() => {
                h2.innerHTML = 'Exito'
                body.appendChild(h2)
            }
        )}else{
            reject(() => {
                h2.innerHTML = 'Cagaste'
                body.appendChild(h2)
            }
        )}
    })


    p.then((mensaje) => {
        mensaje()
        }).catch((mensaje) => {
        mensaje()
        });
}

