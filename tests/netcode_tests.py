from nose.tools import *
from MyIRC.netcode import *

import sys

# Test functions for the netcode

def test_Message():
	testmessage = Message("test message to send", 0)
	
	assert_equal(testmessage.type, 0) 
	assert_equal(testmessage.message, "test message to send")
	assert_equal(testmessage.length, len(str(testmessage)))
	
def test_Socks():
	testsocket = Socks()
	testserver = Server("SocksTest", socket.gethostname(), 12345)
	testsocket.Connect("localhost", testserver.port)
	
def test_Server():
	testserver = Server("test", socket.gethostname(), 12345)
	tempmessage = Message("test message")
	
	assert_equal(testserver.name, "test")
	assert_equal(testserver.address, socket.gethostname())
	assert_equal(testserver.port, 12345)
	
	testserver.ConnectToServer()
	testserver.SendMessage(tempmessage)
	
	
	