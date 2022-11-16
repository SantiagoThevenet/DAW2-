let h2 = document.createElement('h2')
let main = document.getElementById('main')

const comparar = () => {
    let input1 = document.getElementById('input1').value
    let input2 = document.getElementById('input2').value
    input1 = Number(input1)
    input2 = Number(input2)
    h2.textContent = ''
    if (input1 > input2) {
        h2.textContent = `Numero ${input1} es mayor a ${input2}`
    } else if (input1 < input2) {
        h2.textContent = `Numero ${input2} es mayor a ${input1}`
    }else {
        h2.textContent = `Numero ${input2} es igual a ${input1}`
    }
    main.appendChild(h2)
}
