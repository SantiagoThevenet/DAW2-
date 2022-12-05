const comprobar = () => {
    const numTarjeta = document.getElementById('num-tarjeta').value
    const nacimineto = document.getElementById('nacimiento').value
    const cvv = document.getElementById('cvv').value

    const numTarjetaUser = '1234'
    const naciminetoUser = '14/05/2002'
    const cvvUser = '123'

    if (numTarjeta == numTarjetaUser && nacimineto == naciminetoUser && cvv == cvvUser ) {
        const icon = document.getElementById('icon').className = 'fa-solid fa-check'
    }
}