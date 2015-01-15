from nose.tools import *
from MyIRC.netcode import *
from MyIRC.messaging import *

import sys

# Test functions that test class initialization and basic functionality 
# of class members

serverAddress = "Grim-PC"
serverPort = 12345

def test_Message():
	testmessage = Message(0, "TestMessage message")
	
	assert_equal(testmessage.type, 0) 
	assert_equal(testmessage.message, "TestMessage message")
	assert_equal(testmessage.length, len(str(testmessage)))
	assert_equal(testmessage.GetType(), "META")
	
def test_Socks():
	testsocket = Socks()
	testmessage = Message(1, "Socks test message")
	
	assert(testsocket != None)
	testsocket.Connect(serverAddress, serverPort)
	testsocket.Send(testmessage)
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
	
	
	