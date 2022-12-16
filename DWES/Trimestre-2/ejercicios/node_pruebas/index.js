let username = 'luis'
let age = 21
let hasHobbies = false
let points = [1, 2, 3]
let user = {
    name: 'Santi',
    apellido: 'Thevenet'
}

const PI = 3.141516

console.log(username)
console.log(age)
console.log(hasHobbies)
console.log(points)
console.log(user)
console.log(PI)

if (age >= 18) {
    console.log("Bien! Eres un niño grande");
} else {
    console.log("Eres pequeño");
}

const names = ['Pepe', 'Paco', 'Pedro']

for (let i = 0; i < names.length; i++) {
    console.log(names[i]);
}

function showUserInfo(userName, userAges) {
    return `Hola ${userName} ${userAges}`
}

const fshowUserInfo = (userName, userAges) => {
    return `Hola ${userName} ${userAges}`
}


console.log(showUserInfo(username, age))
console.log(fshowUserInfo(username, age))
