# MyIRC README File
This is the README file for the MyIRC (name is a work in progress) client.

This project is a simple IRC client that should be able to connect to 
most IRC servers. MyIRC is written in Python so as to be easily ported to 
multiple platforms.

The file structure and general setup of the project is from 
	learnpythonthehardway.org

## Project Phases
The Project is going to be split into 5 different phases:
<ol>
	<li>Initial project planning and setting up of project files/directories</li>
	<li>Learning about IRC and what will be required to make a functional IRC client.</li>
	<li>Design the client</li>
	<li>Develop and test the client</li>
	<li>Release</li>
</ol>

## Progress so far
### Intial project planning and setup
Installed latest version of python and pylauncher to correctly run the version
of python that I want. This has required me to install the WiX Toolset to build
pylauncher. Wix could be useful at a later stage when building MyIRC.

Python packages nose, distribute and virtualenv have all been installed to assist with
development

## Developer Info
Required packages
<ul>
	<li>Nose</li>
	<li>Virtualenv</li>
	<li>distribute</li>
</ul>

This project is using nosetests to do unit testing.

## File structure

MyIRC/
	MyIRC/
		__init__.py
	bin/
	docs/
	setup.py
	tests/
		MyIRC_tests.py
		__init__.py
		
MyIRC will contain all of the modules containing source code and classes. Bin will be where
the binary or final version of all the code will go after being built. Docs will contain 
data, files and other resources that are required (icons, images, etc). Tests will be where
all of the test modules will be located. Every module in MyIRC should have a respective 
module_test.py file in tests.
