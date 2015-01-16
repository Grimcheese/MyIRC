from nose.tools import *
from MyIRC.src.messaging import *



def test_Message():
	
	# Testing different number of message parameters
	testmessage = Message(0, "CONNECT")
	testmessagtwo = Message(0, "CONNECT", "USERNAME")
	testmessagethree = Message(0, "CONNECT", "USERNAME IP")
	
	assert_equal(testmessage.type, 0) 
	assert_equal(testmessage.message, "CONNECT")
	assert_equal(testmessage.Length(), len(str(testmessage)))
	assert_equal(testmessage.GetType(), "META")
	
	assert_equal(testmessage.parameters, [])
	assert_equal(testmessagtwo.parameters, ["USERNAME"])
	assert_equal(testmessagethree.parameters, ["USERNAME", "IP"])