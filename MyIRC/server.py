import socket
from netcode import Socks

print("TEST SERVER IS NOW UP")

clients = []


serverSocket = Socks()

host = socket.gethostname()
port = 12345
serverSocket.sock.bind((host, port))
serverSocket.sock.listen(5)

# Receiving loop
# Block until a connection is received and then receive data from 
# the new client socket
while True:
	clientSocket, clientAddress = serverSocket.sock.accept()
	
	clientSocket = Socks(clientSocket)
	length = int(clientSocket.sock.recv(14))
	
	data = clientSocket.Receive(length) # Receive up to 1024 bytes from the client
	print(data)
	