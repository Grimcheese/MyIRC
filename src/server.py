import socket
from netcode import *
from messaging import *

print("TEST SERVER STARTING UP")

clientList = []


serverSocket = Socks()

host = socket.gethostname()
port = 12345
serverSocket.sock.bind((host, port))
serverSocket.sock.listen(5)

# Converts a message received via a socket as a string to an actual 
# message object.
def StringToMessageObject(messageString):
	messageParts = messageString.split(Message.delimiter)
	type = eval(messageParts[0])
	str = messageParts[1]
	message = Message(type, str)
	
	return message

# When the server receives a communication message from a client the
# server will send that message to all the other clients that are 
# connected to the server.
def CommunicationMessageHandler(msg):
	pass
	"""for client in clientList:
		
		client.EstablishConnection()
		client.SendMessage(msg)
		client.CloseConnection()
	"""
def MetaMessageHandler(msg):
	print(msg)
	attributes = msg.message.split(" ")
	
	# If a client is requesting a connection to the server
	if attributes[0] == "CONNECT":
		newClient = Client(attributes[1], attributes[2], port)
		clientList.append(newClient)

def MessageHandler(msg):

	if msg.GetType() == "META":
		MetaMessageHandler(msg)
	elif msg.GetType() == "VOICE" or msg.GetType() == "TEXT":
		CommunicationMessageHandler(msg)
	

# Receiving loop
# Block until a connection is received and then receive data from 
# the new client socket

print("Now accepting connections")

while True:
	clientSocket, clientAddress = serverSocket.sock.accept()
	tempClient = Client("TEMPCLIENT", clientAddress[0], clientAddress[1], clientSocket)
	
	msgString = tempClient.ReceiveMessage()
	
	print(msgString)
	# Message is handled
	#clientMessage = StringToMessageObject(msgString)
	#MessageHandler(clientMessage)
	
	# Socket is destroyed
	tempClient.CloseConnection()