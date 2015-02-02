#! python3

import netcode

"""
	Source code that implements messages used to transfer information
	across a network for the MyIRC client and server.
	
	This file contains the implementation for the network protocols 
	of MyIRC.
	
	Classes: 
		Message
		MessageHandler
		ClientMessageHandler
		ServerMessageHandler
		MessageQueue
		
	File also contains miscellaneous helper methods related to messages
		StringToMessageObject
"""


# Class to store network messages
#
# The length is used to indicate to the receiver how long the rest of 
# the message is
#
# Message type indicates how the message should be handled by the client
# Type 0 is meta data
# Type 1 is voice data
# Type 2 is text data		
#
# Parameters is a series of options that are separated by a " " character
class Message(object):
	
	delimiter = '\n'
	
	def __init__(self, type, message, paramString = ""):
		assert type >= 0 and type <= 3
		
		self.type = type
		self.message = message
		self.parameters = []
		if len(paramString) != 0:
			self.parameters = paramString.split(" ")
	
	# Returns the length as an int
	def Length(self):
		return len(str(self))
	
	# Returns the length + the delimiter as a string
	def DelimitedLength(self):
		return str(self.Length()) + Message.delimiter
	
	def GetType(self):
		if self.type == 0:
			typeString = "META"
		elif self.type == 1:
			typeString = "VOICE"
		elif self.type == 2:
			typeString = "TEXT"
			
		return typeString
		
	def __str__(self):
		options = ""
		for option in self.parameters:
			options = options + " " + option
		options = options.lstrip()
		return(str(self.type) + Message.delimiter + self.message + \
		Message.delimiter + options + Message.delimiter)
		
# Abstract MessageHandler class 
class MessageHandler(object):
	
	def __init__(self):
		pass
		
	def HandleMessage(self, message, source):
		pass
		
	def HandleMeta(self, message):
		pass 
		
	def HandleCommunication(self, message):
		pass
		
class ClientMessageHandler(MessageHandler):
	
	def __init__(self):
		super(ClientMessageHandler, self).__init__()
		
	def HandleMessage(self, msg, source):
		if msg.GetType() == "META":
			pass
		elif msg.GetType() == "VOICE":
			pass
		elif msg.GetType() == "TEXT":
			TextMessage(msg, source)
		
	def TextMessage(self, message, source):
		print(message.message)
		
class ServerMessageHandler(MessageHandler):

	def __init__(self):
		super(ServerMessageHandler, self).__init__()
		
	def HandleMessage(self, msg, source, clientlist):
		if msg.GetType() == "META":
			print(msg.message)
			self.HandleMeta(msg, clientlist)
		elif msg.GetType() == "VOICE" or msg.GetType() == "TEXT":
			print(str(source) + ":" + msg.message)
			self.HandleCommunication(msg, source, clientlist)
		
		return clientlist
		
	def HandleCommunication(self, message, source, clientlist):
		for client in clientlist:
			if client.name != source:
				client.EstablishConnection()
				client.SendMessage(message)
				client.CloseConnection()
		
		
	
	def HandleMeta(self, message, clientlist):
		if message.message == "CONNECT":
			newClient = netcode.Client(message.parameters[0], message.parameters[1], eval(message.parameters[2]))
			alreadyconnected = False
			for connectedclient in clientlist:
				if connectedclient.name == newClient.name:
					alreadyconnected = True
			
			if alreadyconnected == False:
				clientlist.append(newClient)
				print("New connection from " + str(newClient))
				# Send acknowledgement to the client
			#else:	
				# Send denial error to the client
			for client in clientlist:
				print(client.name)
			
		return clientlist
	
# The messageQueue is a list of all the messages that have yet to 
# be handled. It should only be accessed using the functions provided:
#	Enqueue(message)
#	Dequeue()
#	Peek()
class MessageQueue(object):
	
	def __init__(self):
		self.messageQueue = []

	# Add a new message to the message queue
	def Enqueue(self, message):
		self.messageQueue.append(message)
	
	def Dequeue(self):
		msg = self.Peek()
		if msg != None:
			return self.messageQueue.pop(0)
		else:
			return None
	
	# Returns the next message in the queue or None
	def Peek(self):
		if len(self.messageQueue) > 0:
			return self.messageQueue[0]
		else:
			return None

# Helper functions for dealing with messages in general
######################################################################


# Converts a string to a message object. 
#
# It is assumed that the string passed to this function is of the form:
#	TYPE\nACTION\nPARAMETERS\n
#	Parameters does not need to be included
def StringToMessageObject(messageString):
	parts = messageString.split(Message.delimiter)
	type = eval(parts[0])
	str = parts[1]
	params = parts[2]

	message = Message(type, str, params)
	
	return message
	
