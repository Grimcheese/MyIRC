#! python3 

import socket
from netcode import *
from messaging import *



# Attempts to connect to the specified server
# Will wait 5 - 10 seconds for a reply from the server
def ConnectToServer(server, username):
	server.EstablishConnection()
	connectMessage = Message(0, "CONNECT", username + " 192.168.1.6 12345")
	server.SendMessage(connectMessage)
	
	server.ReceiveMessage()
	
	server.CloseConnection()
	
	currentServer = server
	
	# If an ack is received add the server to the serverlist
	
def DisconnectFromServer(server, username):
	server.EstablishConnection()
	msg = Message(0, "DISCONNECT", username)
	server.SendMessage(msg)
	server.CloseConnection()

def GetServer(name, serverList):
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
def Commands(str, settings):
	list = str.split(" ")
	command = list[0]
	
	parameters = len(list) - 1
	# Command handler
	if command == "/connect":
		# no parameters
		if parameters == 0:
			ConnectToServer(settings[1], settings[0])
		elif parameters == 1:
			ConnectToServer(GetServer(list[1], settings[2]), settings[0])
		elif parameters == 3:
			newServer = Server(list[1], list[2], eval(list[3]))
			ConnectToServer(newServer, settings[0])
		else:
			print("Invalid number of parameters")
	elif command == "/disconnect":
		if parameters == 0:
			DisconnectFromServer(settings[1], settings[0])
		elif parameters == 1:
			DisconnectFromServer(GetServer(list[1], settings[2]), settings[0])
		else:
			print("Invalid number of parameters")
	else:
		print("Not a valid command")
			
def ParseString(str, settings):
	if len(str) > 0:
		if str[0] == "/":
			Commands(str, settings)
		else:
			if currentServer != None:
				currentServer = settings[1]
				msgStr = "2\n" + str + "\n" + settings[0] + "\n"
				currentServer.EstablishConnection()
				currentServer.SendMessage(StringToMessageObject(msgStr))
				currentServer.CloseConnection()
			
def Startup(userName, currentServer, serverList, defaultServer):
	print("Welcome to MyIRC")
	# Load previous settings
	# Show previous settings to user
	# Ask if use previous or make new settings
	userName = input("Set username: ")
	
	return [userName, currentServer, serverList, defaultServer]
	
def main():
	serverList = []
	defaultServer = Server("Test Server", socket.gethostname(), 12345)
	serverList.append(defaultServer)
	currentServer = defaultServer
	Username = "Alby"
	
	prompt = str(currentServer) + ": "

	settings = Startup(Username, currentServer, serverList, defaultServer)
	
	userStr = input(prompt)
	while userStr != "exit":
		ParseString(userStr, settings)
		userStr = input(prompt)
main()