from nose.tools import *
from MyIRC.netcode import *

import sys

# Test functions for the netcode

def test_message():
	testmessage = Message("test message to send", 0)
	
	assert_equal(testmessage.type, 0) 
	assert_equal(testmessage.message, "test message to send")
	assert_equal(testmessage.length, sys.getsizeof(str(testmessage)))