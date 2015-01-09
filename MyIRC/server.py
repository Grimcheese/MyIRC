import socket

s = socket.socket()

host = s.getHostName()
port = 12345
s.bind(