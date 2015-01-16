from nose.tools import *
from MyIRC.src.netcode import *
from MyIRC.src.messaging import *

import sys

# Test functions that test class initialization and basic functionality 
# of class members

serverAddress = "Grim-PC"
serverPort = 12345
	
def test_Socks():
	testsocket = Socks()
	testmessage = Message(1, "Socks test message")
	
	assert(testsocket != None)
	testsocket.Connect(serverAddress, serverPort)
	testsocket.Send("1\n", 2)
	testsocket.Send("a", 1)
	testsocket.Disconnect()
	
def test_BaseClient():
	testAddress = socket.gethostname()
	testPort = 12345

	testBaseClient = BaseClient("TestBaseClient", testAddress, testPort)
	
	assert_equal(testBaseClient.name, "TestBaseClient")
	assert_equal(testBaseClient.address, testAddress)
	assert_equal(testBaseClient.port, testPort)
	
	testmessage = Message(0, "BaseClient message test")
	
	testBaseClient.EstablishConnection()
	testBaseClient.SendMessage(testmessage)
	testBaseClient.CloseConnection()
	
def test_Server():
	testserver = Server("testserver", serverAddress, serverPort)
	tempmessage = Message(0, "ServerTestMessage")
	
	assert_equal(testserver.name, "testserver")
	assert_equal(testserver.address, serverAddress)
	assert_equal(testserver.port, serverPort)
	
	
	