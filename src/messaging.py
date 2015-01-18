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
	
	def __init__(self, type, message, params = ""):
		assert type >= 0 and type <= 3
		
		self.type = type
		self.message = message
		self.parameters = []
		if len(params) != 0:
			self.parameters = params.split(" ")
	
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
		

class MessageHandler(object):
	pass
		
# The messageQueue is a list of all the messages that have yet to 
# be handled. It should only be accessed using the functions provided:
#	Enqueue(message)
#	Dequeue()
#	Peek()
class MessageQueue(object):
	
	def __init__(self):
		self.messageQueue = []

	# Add a new message to the message queue
	def Enqueue(message):
		self.messageQueue.append(message)
	
	def Dequeue():
		msg = Peek()
		if msg != None:
			return self.messageQueue.pop(0)
		else:
			return None
	
	# Returns the next message in the queue or None
	def Peek()
		if self.SizeOfQueue() > 0:
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
	params = parts[2].split(" ")

	message = Message(type, str, params)
	
	return message
	
