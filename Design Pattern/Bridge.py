"""Implementation of Bridge pattern"""
from abc import ABCMeta, abstractmethod

class Implementor:
	"""The abstract class of Implementor"""
	__metaclass__ = ABCMeta
	
	@abstractmethod
	def operation(self):pass
	
class ConcreteImplementorA(Implementor):
	"""The class of concrete Implementor A"""
	def operation(self):
		print " the method of Concrete Implementor A operated"

		
class ConcreteImplementorB(Implementor):
	"""The class of concrete Implementor B"""
	def operation(self):
		print " the method of Concrete Implementor B operated"
		
class Abstraction:
	""" The class of Abstraction"""
	__metaclass__ = ABCMeta
	
	def __init__(self):
		self._imp = None
	
	def setImplementor(self, imp):
		self._imp = imp
	
	@abstractmethod
	def operation(self):pass
	
class RefinedAbstraction(Abstraction):
	""" The class of refined Abstraction"""
	def __init__(self):
		Abstraction.__init__(self)
	
	def operation(self):
		self._imp.operation()
		
if __name__ == '__main__':
	ab = RefinedAbstraction()
	ab.setImplementor(ConcreteImplementorA())
	ab.operation()
	ab.setImplementor(ConcreteImplementorB())
	ab.operation()
	
	
