from nose.tools import *
from MyIRC.src.messaging import *



def test_Message():
	testmessage = Message(0, "TestMessage message")
	
	assert_equal(testmessage.type, 0) 
	assert_equal(testmessage.message, "TestMessage message")
	assert_equal(testmessage.Length(), len(str(testmessage)))
	assert_equal(testmessage.GetType(), "META")