import socket
from netcode import Server

testserver = Server("Test Server", socket.gethostname(), 12345)

testserver.ConnectToServer()
testserver.SendMessage("Testing, one two three.")
testserver.DisconnectFromServer()

