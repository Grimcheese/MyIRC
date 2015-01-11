import socket



clients = []


serverSocket = socket.socket()

host = socket.gethostname()
port = 12345
serverSocket.bind((host, port))
serverSocket.listen(5)

# Receiving loop
# Block until a connection is received and then receive data from 
# the new client socket
while True:
	clientSocket, clientAddress = serverSocket.accept()
	
	data = clientSocket.recv(1024) # Receive up to 1024 bytes from the client
	
	print(data)
	
class Client(object):
	