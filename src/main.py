import socket
from netcode import *
from messaging import *

server = Server("Test Server", socket.gethostname(), 12345)



def ConnectToServer(server):
	server.EstablishConnection()
	connectMessage = Message(0, "CONNECT", "Alby 192.168.1.6, 12345")
	server.SendMessage(connectMessage)
	server.CloseConnection()
	
ConnectToServer(server)