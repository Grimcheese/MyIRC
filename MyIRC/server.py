import socket
from netcode import Socks, Message, Server, BaseClient

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
	testClient = BaseClient("CLIENT", clientAddress[0], clientAddress[1], clientSocket)
	
	data = testClient.ReceiveMessage()
	
	# Message is handled
	print(data)
	
	# Socket is destroyed
	testClient.CloseConnection()
