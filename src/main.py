#! python3 

import socket
from netcode import *
from messaging import *

serverList = []
defaultServer = Server("Test Server", socket.gethostname(), 12345)
serverList.append(defaultServer)

Username = "Alby"

# Attempts to connect to the specified server
# Will wait 5 - 10 seconds for a reply from the server
def ConnectToServer(server):
	server.EstablishConnection()
	connectMessage = Message(0, "CONNECT", "Alby 192.168.1.6 12345")
	server.SendMessage(connectMessage)
	server.CloseConnection()
	
	# If an ack is received add the server to the serverlist
	
def DisconnectFromServer(server):
	server.EstablishConnection()
	msg = Message(0, "DISCONNECT", Username)
	server.SendMessage(msg)
	server.CloseConnection()

def GetServer(name):
	for server in serverList:
		if server.name == name:
			return server
			
# Method to handle commands input by the user. 
#
# Commands always begin with a forward slash (/) and can be followed
# by parameters separated by a space character
#
# Supported Commands
# 	/connect
#		/connect
#		/connect servername
#		/connect servername hostname serverport
#	/disconnect
#		/disconnect
#		/disconnect servername
def Commands(str):
	list = str.split(" ")
	command = list[0]
	
	parameters = len(list) - 1
	# Command handler
	if command == "/connect":
		# no parameters
		if parameters == 0:
			ConnectToServer(defaultServer)
			currentServer = defaultServer
		elif parameters == 1:
			ConnectToServer(GetServer(list[1]))
		elif parameters == 3:
			newServer = Server(list[1], list[2], list[3])
			ConnectToServer(newServer)
		else:
			print("Invalid number of parameters")
	elif command == "/disconnect":
		if parameters == 0:
			DisconnectFromServer(currentServer)
		elif parameters == 1:
			DisconnectFromServer(GetServer(list[1]))
		else:
			print("Invalid number of parameters")
	else:
		print("Not a valid command")
			
def ParseString(str):
	if len(str) > 0:
		if str[0] == "/":
			Commands(str)
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
	