const apiKey = "BicpeL2IwuxQGgKMkYALcAwadhFUNdwR";

const url = `https://api.giphy.com/v1/gifs/random?apikey=${apiKey}`;

axios.get(url)
    .then((response) => {
        let datos = response => {
            const body = document.body
            const section = document.createElement('section')

            body.appendChild(section)

            const h1 = document.createElement('h1')
            const img = document.createElement('img')
            const h3user = document.createElement('h3')
            const h3titulo = document.createElement('h3')
            const button = document.createElement('button')
            
            h1.textContent = 'GIFS'
            img.src = mensaje.data.images.downsized_medium.url
            h3user.textContent = mensaje.data.username
            h3titulo.textContent = mensaje.data.title
            button.textContent = 'Reset'
            
            section.appendChild(h1)
            section.appendChild(img)
            section.appendChild(h3user)
            section.appendChild(h3titulo)
            section.appendChild(button)

            // button.addEventListener('click', () => location.reload())
            button.setAttribute('onclick', 'location.reload()')
            
            
        });
    })
    .catch((res) => {
        console.log(res);
    });






