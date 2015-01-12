import socket
from netcode import Server, Message

testserver = Server("Test Server", socket.gethostname(), 12345)

msg = Message("Doing test things and such")



def ConnectToServer(server):
	server.EstablishConnection()
	connectMessage = Message("CONNECT", 0)
	server.SendMessage(connectMessage)
	server.CloseConnection()
	
ConnectToServer(testserver)