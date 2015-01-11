import socket
from netcode import Socks, Message

print("TEST SERVER IS NOW UP")

clients = []


serverSocket = Socks()

host = socket.gethostname()
port = 12345
serverSocket.sock.bind((host, port))
serverSocket.sock.listen(5)

def GetMessageLength(sock):
	bits = []
	bit = 'a'
	while bit != ":":
		bit = sock.Receive(1)
		if bit != ":":
			bits.append(bit)
			
	return ''.join(bits)


# Receiving loop
# Block until a connection is received and then receive data from 
# the new client socket
while True:
	clientSocket, clientAddress = serverSocket.sock.accept()
	clientSocket = Socks(clientSocket)
	
	# Get the length of the incoming message
	length = int(GetMessageLength(clientSocket))
	
	data = clientSocket.Receive(length) 
	print(data)
	
