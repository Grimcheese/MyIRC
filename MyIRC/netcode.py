import socket

class Socks(object):
	
	def __init__(self, s = None):
		if s is None:
			self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		else:
			self.s = s
			
	# Should be passing server object not host and port
	def ConnectToServer(self, host, port):
		self.s.connect((host, port))
	
	def DisconnectFromServer(self):
		self.s.close()
		
	def SendMessage(self, message):
		self.s.send(message)

	def ReceieveMessage(self):
		return(self.s.recv(1024))
		
# Contains basic information about a server that the user is connected
# to.
class Server(object):
	
	def __init__(self):