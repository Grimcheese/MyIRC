from messaging import Message

import socket, sys

"""
	Source file for networking code related to MyIRC
	
	Contains the following classes:
		Socks
			Basic socket class used to interface with socket
		BaseClient
			Contains basic client info; name, address etc.
		Client/Server
			Wrapper classes for BaseClient. Used to differentiate a 
			BaseClient between a server and an actual client.
			Adds Client/Server functionality to the BaseClient
			
"""



# Basic socket object that acts as an interface between MyIRC and 
# socket. 
# Provides easy to use Send and Receive methods that ensure
# all of a message is sent or received before moving on.
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
	def Send(self, messageStr, length):
		# Send the message
		totalsent = 0
		encodedMsg = messageStr.encode()
		while totalsent < length:
			sent = self.sock.send(encodedMsg[totalsent:])
			if sent == 0:
				raise RuntimeError("Connection broken")
			totalsent = totalsent + sent
	
	def Receive(self, length):
		chunks = []
		bytes_recd = 0
		
		while bytes_recd < length:
			chunk = self.sock.recv(min(length - bytes_recd, 2048))
			chunk = chunk.decode()
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
	# Note that a new Socks object is only created if one is not 
	# already instantiate
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
		self.sock.Send(message.DelimitedLength(), len(message.DelimitedLength()))
		self.sock.Send(str(message), message.Length())

	def ReceiveMessage(self):
		length = int(self._GetMessageLength(self.sock))
		message = self.sock.Receive(length)
		return message
		
	def _GetMessageLength(self, sock):
		bits = []
		bit = ''
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
		self.clientList = []
	
class Client(BaseClient):
	
	def __init__(self, name, address, port, sock = None):
		super(Client, self).__init__(name, address, port, sock)
		self.serverList = []