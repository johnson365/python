""" Implementation of the Prototype pattern"""
from abc import ABCMeta, abstractmethod
from copy import deepcopy, copy

copyfunc = deepcopy
class Prototype:
	""" Prototype class """
	__metaclass__ = ABCMeta
	
	def __init__(self, id):
		self.id = id
	
	def getId(self):
		return self.id
	
	@abstractmethod
	def clone(self):pass
	
class ConcretePrototype(Prototype):

	def clone(self):
                cp = (Prototype)copyier(self)
		return cp

		
if __name__ == '__main__':
	cp = ConcretePrototype('I')
	cp2 = cp.clone()
	print(cp2.id)
