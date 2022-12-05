import socket 

PORT = 65436
with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as s:
    s.bind(('localhost',PORT))
    s.listen()
    cont = 0
    print(f'Servidor abierto: http://localhost:{PORT}/')
    while True:
        conn, addr = s.accept()
        with conn:
            recive = conn.recv(2048)
            if cont == 0:
                with open('./index.html', 'r') as html:
                    e = html.read()  
                    conn.send(f'HTTP/1.1 200 OK \r\nContent-type: text/html\r\n\r\n {e}'.encode())
            elif cont == 1:
                with open('./style.css', 'r') as css:
                    c = css.read()
                    conn.send(f'HTTP/1.1 200 OK \r\nContent-type: text/css\r\n\r\n {c}'.encode())
            elif cont == 2:
                with open('./img.jpg', 'rb') as img:
                    i = img.read()
                    conn.send(b'HTTP/1.1 200 OK \r\nContent-type: image/jpeg\r\n\r\n'+i)

            cont += 1
