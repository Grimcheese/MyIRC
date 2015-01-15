# Class to store network messages
#
# The length is used to indicate to the receiver how long the rest of 
# the message is
#
# Message type indicates how the message should be handled by the client
# Type 0 is meta data
# Type 1 is voice data
# Type 2 is text data		
class Message(object):
	
	delimiter = '\n'
	
	def __init__(self, type, message):
		assert type >= 0 and type <= 3
		
		self.type = type
		self.message = message
		self.length = len(str(self))
		
	def GetType(self):
		if self.type == 0:
			typeString = "META"
		elif self.type == 1:
			typeString = "VOICE"
		elif self.type == 2:
			typeString = "TEXT"
			
		return typeString
		
	def __str__(self):
		return(str(self.type) + Message.delimiter + self.message)			