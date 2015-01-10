import socket

class Socks(object):
	
	def __init__(self, s = None):
		if s is None:
			self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		else:
			self.s = s
			
	# Connects to a server using the server's address and port members
	def ConnectToServer(self, server):
		self.s.connect((server.get(address), server.get(port)))
	
	def DisconnectFromServer(self):
		self.s.close()
		
	def SendMessage(self, message):
		self.s.send(message)

	def ReceieveMessage(self):
		return(self.s.recv(1024))
		
# Contains basic information about a server that the user is connected
# to.
class Server(object):
	
	def __init__(self, name, address, port):
		self.name = name
		self.address = address
		self.port = port