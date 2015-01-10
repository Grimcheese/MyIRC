import socket

# Contains basic information about a server that the user is connected
# to. Stores the socket and facilitates communication between the client
# and the server.
class Server(object):
	
	def __init__(self, name, address, port, s = None):
		self.name = name
		self.address = address
		self.port = port
		
		if s is None:
			self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		else:
			self.s = s
			
	# Connects to a server using the server's address and port members
	def ConnectToServer(self):
		self.s.connect((self.address, self.port))
	
	def DisconnectFromServer(self):
		self.s.close()
		
	def SendMessage(self, message):
		self.s.send(message)

	def ReceieveMessage(self):
		return(self.s.recv(1024))