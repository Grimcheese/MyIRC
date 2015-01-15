import socket, sys


# My basic socket object to handle connections between sockets
class Socks(object):
	def __init__(self, sock = None):
		if sock is None:
			self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		else:
			self.sock = sock
	
	# Establishes a connection with the hostname and port 
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
		self.sock.send(str(message.length).encode() + b":")
	
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
		
# Contains basic information for a client. Note that a client could
# also refer to a server.
#
# Contains name, IP/hostname and the port that refers to the client.
# Can also contain a socket that is used during transmissions.
#
# Class relationships
#	Has-a Socks (socket) object as an attribute
#	Uses a message object to pass to the socket for transmission
#
# A new Socks object is created for each transmission.
class BaseClient(object):
	
	def __init__(self, name, address, port, sock = None):
		self.name = name
		self.address = address
		self.port = port
		
		if sock is None:
			self.sock = None
		else:
			self.sock = Socks(sock)
	
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

	def ReceiveMessage(self):
		length = int(self._GetMessageLength(self.sock))
		message = self.sock.Receive(length)
		return message
		
	def _GetMessageLength(self, sock):
		bits = []
		bit = '0'
		while bit != Message.delimiter:
			bit = sock.Receive(1)
			if bit != Message.delimiter:
				bits.append(bit)
				
		return ''.join(bits)	
		
	##################################################################

# Server client class
#
# Inherits from BaseClient
class Server(BaseClient):
	
	def __init__(self, name, address, port, sock = None):
		super(Server, self).__init__(name, address, port, sock)
	
class Client(BaseClient):
	
	def __init__(self, name, address, port, sock = None):
		super(Client, self).__init__(name, address, port, sock)
		

	# Class to store network messages
#
# The length is used to indicate to the receiver how long the rest of 
# the message is
#
# Message type indicates how the message should be handled by the client
# Type 0 is meta data
# Type 1 is voice data
# Type 2 is text data		
class Message(object):
	
	delimiter = '\n'
	
	def __init__(self, type, message):
		assert type >= 0 and type <= 3
		
		self.type = type
		self.message = message
		self.length = len(str(self))
		
	def GetType(self):
		if self.type == 0:
			typeString = "META"
		elif self.type == 1:
			typeString = "VOICE"
		elif self.type == 2:
			typeString = "TEXT"
			
		return typeString
		
	def __str__(self):
		return(str(self.type) + Message.delimiter + self.message)			