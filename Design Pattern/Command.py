"""Implementation of Command pattern"""
from abc import ABCMeta, abstractmethod

class Command:
	"""The abstract class of Command"""
	__metaclass__ = ABCMeta
	
	def __init__(self, recv):
		self._recv = recv # _recv is a protected attribute
		
	@abstractmethod
	def execute(self):pass
	
class ConcreteCommand(Command):
	"""The concrete class of Command """
	def __init__(self, recv):
		Command.__init__(self, recv)
		
	def execute(self):
		self._recv.action()
		
class Invoker:
	""" The class of Invoker which ask command to execute the request """
	
	def __init__(self):
		self.__com = None #__com is a private attribute
		
	def setCommand(self, com):	
		self.__com = com
	
	def executeCommand(self):
		self.__com.execute()
		
class Receiver:
	"""The class of Receiver"""
	
	def action(self):
		print "Execute request!"
		
if __name__ == '__main__':
	r = Receiver()
	c =ConcreteCommand(r)
	i = Invoker()
	i.setCommand(c)
	i.executeCommand()