const http = require('http')

// request escucha al cliente
// request responde al clinte

const server = http.createServer((request, response) => {
    response.setHeader('Content-Type','text/html; charset = utf-8')

    if (request.url === '/') {
        response.write('Hola')
        return response.end()
    }
    if (request.url === '/about') {
        response.write('Estas en about')
        return response.end()
    }
    response.write('<h1>Not found</h1>')
    response.write('<h2>Esta pagina no se encontro</h2>')
    response.write('<a href="/">Volver al inicio</a>')
    return response.end()
})

server.listen(3000)

console.log("Servidor escuchando en el puerto 3000");
