import socket
from netcode import Server, Message

testserver = Server("Test Server", socket.gethostname(), 12345)

msg = Message("Doing test things and such")

testserver.ConnectToServer()
testserver.SendMessage(msg)
testserver.DisconnectFromServer()

