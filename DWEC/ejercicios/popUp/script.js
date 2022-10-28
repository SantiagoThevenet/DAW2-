const div = document.getElementById('popup')
const button = document.getElementById('button')
div.style.display = 'none'

const cick = () => {
    div.style.display = 'flex'
    button.style.display = 'none'
}

const cruz = () => {
    div.style.display = 'none'
    button.style.display = 'flex'
}