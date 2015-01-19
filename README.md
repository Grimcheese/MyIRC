# MyIRC README File
This is the README file for MyIRC (name is a work in progress). 

v0.1


## Project Brief
This project is a simple voip/chat client that will be able to connect 
to an MyIRC server. MyIRC is intended to be similar to other voip 
clients such as Ventrilo or Mumble in that it gives users the ability
to communicate over both mediums of voice and text.

Text chat should be easy to use and convenient for users to go with or
without it while using voip as the main feature.

The user should be able to connect to a server only using text, voice 
or both. The user should also be able to connect to multiple servers 
simultaneously. 

## Project Phases
The Project is going to be split into 5 different phases:
<ol>
	<li>Initial project planning and setting up of project 
	files/directories</li>
	<li>Learning about voip and text chat and what will be required to 
	make a functional client.</li>
	<li>Design the client</li>
	<li>Develop and test the client</li>
	<li>Release</li>
</ol>

## Progress so far
### Intial project planning and setup
Installed latest version of python and pylauncher to correctly run the
version
of python that I want. This has required me to install the WiX Toolset 
to build pylauncher. Wix could be useful at a later stage when 
building MyIRC.

Python packages nose, distribute and virtualenv have all been installed 
to assist with development

## Developer Info
Required packages
<ul>
	<li>Nose</li>
	<li>Virtualenv</li>
	<li>distribute</li>
</ul>

This project is using nosetests to do unit testing.

### Coding conventions
All text is written with a 70 character length so as to fit with the 
way my current environment is setup (notepad++ with multiple files and
a command line on one monitor)

<ol>
	<li>Function names use camel case beginning with a lower case 
	letter (exampleFunctionNameHere) </li>
	<li>Class names use camel case beginning with a capital letter 
	(ExampleClassNameHere)</li>
	<li>Tabs are set to 4 spaces</li>
</ol>
## File structure

MyIRC/<br />
<nbsp>MyIRC/
		__init__.py
	bin/
	docs/
	setup.py
	tests/
		MyIRC_tests.py
		__init__.py
		
The file structure and general setup of the project is from 
	learnpythonthehardway.org

		
MyIRC will contain all of the modules containing source code and classes.
Bin will be where the binary or final version of all the code will go 
after being built. Docs will contain data, files and other resources 
that are required (icons, images, etc). Tests will be where all of 
the test modules will be located. Every module in MyIRC should have a 
respective module_test.py file in tests.