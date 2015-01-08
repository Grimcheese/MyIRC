try:
	from setuptools import setuptools
except ImportError:
	from distutils.core import setup
	
config = {
	'description' : 'IRC client being developed in the Python programming language',
	'author' : 'Alby Chawula',
	'url' : 'no url'
	'version' : '0.1',
	'install_requires' : ['nose'],
	'packages' : ['MyIRC'],
	'scripts' : [],
	'name' : 'MyIRC'
}

setup(**config)