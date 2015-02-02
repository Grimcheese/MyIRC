#! python3 

import socket
from netcode import *
from messaging import *

serverList = []
server = Server("Test Server", socket.gethostname(), 12345)
serverList.append(server)
currentServer = serverList[0]
Username = "Alby"

# Attempts to connect to the specified server
# Will wait 5 - 10 seconds for a reply from the server
def ConnectToServer(server):
	server.EstablishConnection()
	connectMessage = Message(0, "CONNECT", "Alby 192.168.1.6 12345")
	server.SendMessage(connectMessage)
	server.CloseConnection()
	
def ParseString(str):
	if len(str) > 0:
		if str[0] == "/":
			if str == "/connect":
				ConnectToServer(server)
			# This is a command
		else:
			msgStr = "2\n" + str + "\n" + Username + "\n"
			currentServer.EstablishConnection()
			currentServer.SendMessage(StringToMessageObject(msgStr))
			currentServer.CloseConnection()

print("Welcome to MyIRC")
prompt = str(currentServer) + ":"
userStr = input(prompt)
while userStr != "exit":
	ParseString(userStr)
	userStr = input(prompt)
	