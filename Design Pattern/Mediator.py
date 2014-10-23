"""Implementation of Chain of Mediator pattern"""
from abc import ABCMeta, abstractmethod

class Mediator(object):
	""" The abstract class of Mediator"""
	__metaclass__ = ABCMeta
	
	@abstractmethod
	def send(self, msg, col):pass
	
class Colleague(object):
	""" The abstract class of Colleague """
	__metaclass__ = ABCMeta
	
	def __init__(self, mediator):
		self._mediator = mediator # _mediator is a protected attribute
		
class ConcreteMediator(Mediator):
	""" The class of concrete Mediator """
	
	def __init__(self):
		self.__col1 = None
		self.__col2 = None
	
	def setCol1(self, col):
		self.__col1 = col
	
	def getCol1(self):
		return self.__col1
		
	def setCol2(self, col):
		self.__col2 = col
	
	def getCol2(self):
		return self.__col2
		
	def send(self, msg, col):
		if col == self.__col1:
			self.__col2.notify(msg)
		else:
			self.__col1.notify(msg)
			

class ConcreteColleague1(Colleague):
	""" the class of concrete Colleague 1"""
	
	def __init__(self, mediator):
		Colleague.__init__(self, mediator)
		
	def send(self, msg):
		self._mediator.send(msg, self)
	
	def notify(self, msg):
		print "Colleague1 got the message:%s" % (msg)
		
class ConcreteColleague2(Colleague):
	""" the class of concrete Colleague 1"""
	
	def __init__(self, mediator):
		Colleague.__init__(self, mediator)
		
	def send(self, msg):
		self._mediator.send(msg, self)
	
	def notify(self, msg):
		print "Colleague2 got the message:%s" % (msg)
		
if __name__ == '__main__':

	m = ConcreteMediator()
	c1 = ConcreteColleague1(m)
	c2 = ConcreteColleague2(m)
	m.setCol1(c1)
	m.setCol2(c2)
	c1.send('how are you?')
	c2.send('fine, thank you! and you ?')
