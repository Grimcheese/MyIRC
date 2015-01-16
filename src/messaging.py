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
	
	def __init__(self, type, message, params = []):
		assert type >= 0 and type <= 3
		
		self.type = type
		self.message = message
		if len(params) == 0:
			self.parameters = []
		else:
			self.parameters = params
	
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
		Message.delimiter + options)
		
# Class to handle messages that are received. TODO!!!
class MessageHandler(object):
	pass
	
