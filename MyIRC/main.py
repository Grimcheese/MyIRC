import socket
from netcode import Socks



server = Socks()

server.ConnectToServer(socket.gethostname(),12345)
server.SendMessage("Testing, one two three.")
server.DisconnectFromServer()

