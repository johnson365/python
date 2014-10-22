"""Implementation of State pattern"""
from abc import ABCMeta, abstractmethod

class State:
	""" The abstract class of State"""
	__metaclass__ = ABCMeta
	
	@abstractmethod
	def handle(self, context):pass
	
class ConcreteStateA(State):
	""" The concrete State class A"""
	
	def handle(self, context):
		print "The state is changing from state A to state B"
		context.state = ConcreteStateB()
		
class ConcreteStateB(State):
	""" The concrete State class B"""
	
	def handle(self, context):
		print "The state is changing from state B to state A"
		context.state = ConcreteStateA()

class Context:
	""" The class of Context """
	
	def __init__(self, state):
		self.__state = state
	
	def getState(self):
		return self.__state
	
	def setState(self, state):
		self.__state = state
		
	def requestChange(self):
		self.__state.handle(self)
		
if __name__ == '__main__':
	c = Context(ConcreteStateA())
	
	c.requestChange();
	c.requestChange();
	c.requestChange();
	c.requestChange();
