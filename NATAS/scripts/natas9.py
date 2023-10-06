import socket


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind(('192.168.0.135', 5554))
    s.listen(1)
    conn, addr = s.accept()
    with conn as c:
        print("connected, now receiving")
        data = c.recv(1024).decode()
    
print(data)