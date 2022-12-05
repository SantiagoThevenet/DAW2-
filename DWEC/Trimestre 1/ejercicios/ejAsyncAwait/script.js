const body = document.body

let multiplicar = (numero) => {
    for (let i = 1; i < 11; i++) {
        const p = document.createElement('p')
        p.textContent = `${numero} * ${i} = ${numero*i}`
        
        setTimeout(() => {
            body.appendChild(p)
        }, 1000*i);
    }
}

let contador = 0
let mi_funcion = () => {
    if (contador === 0) {
        return new Promise((resolve, reject) => {
            let num = document.getElementById('input').value
            if (num != '') {
                if (num >= 0 && num <= 10) {
                    resolve(multiplicar(num))
                } 
            }
        })
    }
    contador++

}



let miFuncionAsincrona = async () => {
    await mi_funcion()
}

miFuncionAsincrona()