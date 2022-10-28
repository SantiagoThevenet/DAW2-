import socket 
with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as s:
    s.bind(('localhost',65431))
    s.listen()
    while True:
        conn, addr = s.accept()
        with conn:
            recive = conn.recv(2048)
            print(recive)
            if b'.html' in recive:
                with open('./index.html', 'r') as html:
                    e = html.read()  
                    conn.send(f'HTTP/1.1 200 OK \r\nContent-type: text/html\r\n\r\n {e}'.encode())
            elif b'.css' in recive:
                with open('./style.css', 'r') as css:
                    c = css.read()
                    conn.send(f'HTTP/1.1 200 OK \r\nContent-type: text/css\r\n\r\n {c}'.encode())
            elif b'.jpg' in recive:
                with open('./img.jpg', 'rb') as img:
                    i = img.read()
                    conn.send(b'HTTP/1.1 200 OK \r\nContent-type: image/jpeg\r\n\r\n'+i)


