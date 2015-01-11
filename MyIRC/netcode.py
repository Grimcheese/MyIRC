import socket, sys


# My basic socket object to handle connections between sockets
class Socks(object):
	def __init__(self, sock = None):
		if sock is None:
			self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		else:
			self.sock = sock
	
	# Establishes a connection with the host and port 
	def Connect(self, host, port):
		self.sock.connect((host, port))
		
	# Disconnects the socket and closes it. CAN NO LONGER BE USED
	def Disconnect(self):
		self.sock.close()
		del self.sock
		
	# Sends the message object to the connected socket
	# This function assumes that the socket has already been connected
	# using the Connect() function
	def Send(self, message):
		# Send the length
		self.sock.send(str(message.length).encode() + ":")
	
		# Send the message
		totalsent = 0
		encodedMsg = str(message).encode()
		while totalsent < message.length:
			sent = self.sock.send(encodedMsg[totalsent:])
			if sent == 0:
				raise RuntimeError("Connection broken")
			totalsent = totalsent + sent
	
	def Receive(self, length):
		chunks = []
		bytes_recd = 0
		
		while bytes_recd < length:
			chunk = self.sock.recv(min(length - bytes_recd, 2048))
			if chunk == '':
				raise RuntimeError("Connection lost")
			chunks.append(chunk)
			bytes_recd = bytes_recd + len(chunk)
		return ''.join(chunks)
		
# Contains basic information about a server that the user is connected
# to. Stores the socket and facilitates communication between the client
# and the server.

# Class relationships
#	Has-a Socks (socket) object as an attribute
#	Uses a message object to pass to the socket for transmission
#
# sock is not instantiated until actually connecting to the server.
class Server(object):
	
	def __init__(self, name, address, port, sock = None):
		self.name = name
		self.address = address
		self.port = port
		
		self.sock = sock
	
	##################################################################
	# The following methods use the Socks class 
	##################################################################
	
	# Connects to and instantiates the server socket using the server's 
	# address and port which are provided by the user.
	#
	# Note that a new Socks object is only created if Server does not 
	# already have a Socks object
	def EstablishConnection(self):
		self.sock = Socks(self.sock) 
		self.sock.Connect(self.address, self.port)
	
	# CLoses the socket and sets sock to None so if there are any 
	# future connections with the Server object a new socket can be
	# created
	def CloseConnection(self):
		self.sock.Disconnect()
		self.sock = None
		
	def SendMessage(self, message):
		self.sock.Send(message)

	def ReceieveMessage(self):
		message = self.sock.Receive()
		
	##################################################################
# Class to store network messages

# Message type indicates how the message should be handled by the client
# Type 0 is meta data
# Type 1 is voice data
# Type 2 is text data		
class Message(object):
	
	def __init__(self, message, type = 0):
		self.type = type
		self.message = message
		self.length = len(str(self))
		
	def __str__(self):
		return(str(self.type) + ":" + self.message)
		
	#def ConvertToMessage(inString):
	#	for i in inString: