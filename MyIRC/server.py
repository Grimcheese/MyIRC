import socket

serverSocket = socket.socket()

host = socket.getHostName()
port = 12345
serverSocket.bind((host, port))
serverSocket.listen(5)

while True:
	clientSocket, clientAddress = serverSocket.accept()