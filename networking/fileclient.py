import socket

s = socket.socket()

s.connect(("localhost",6767))

fileName = input("enter a filename: ")

s.send(fileName.encode())

content = s.recv(1024)

print(content.decode())
    
s.close()