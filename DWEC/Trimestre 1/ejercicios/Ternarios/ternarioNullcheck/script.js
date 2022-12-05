const enviarInfo = () => {

    const nombre = document.getElementById('nombre').value
    const apellido = document.getElementById('apellido').value
    const date = document.getElementById('date').value
    const opcion = document.getElementById('opcion').value
    
 
   
    swal(`${nombre||'Vacío'}\n${apellido||'Vacío'}\n${date||'Vacío'}\n${opcion||'Vacío'}`)
}


