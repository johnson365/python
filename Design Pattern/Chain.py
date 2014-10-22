"""Implementation of Chain of Responsibility pattern"""
from abc import ABCMeta, abstractmethod

class Handler:
	"""The abstract class of Handler """
	__metaclass__ = ABCMeta
	
	def __init__(self):
		self._handler = None # _handler is a protected attribute
		
	def setHandler(self, handler):
		self._handler = handler
		
	@abstractmethod
	def handleRequest(self, request):pass
	
class ConcreteHandler1(Handler):
	
	def handleRequest(self, request):
		if 0 <= request < 10:
			print "ConcreteHandler1 handle request %d" % (request)
		elif self._handler != None:
			self._handler.handleRequest(request)
			
class ConcreteHandler2(Handler):
	
	def handleRequest(self, request):
		if 10 <= request < 20:
			print "ConcreteHandler2 handle request %d" % (request)
		elif self._handler != None:
			self._handler.handleRequest(request)
			
class ConcreteHandler3(Handler):
	
	def handleRequest(self, request):
		if 20 <= request < 30:
			print "ConcreteHandler3 handle request %d" % (request)
		elif self._handler != None:
			self._handler.handleRequest(request)
			
if __name__ == '__main__':
	h1 = ConcreteHandler1()
	h2 = ConcreteHandler2()
	h3 = ConcreteHandler3()
	h1.setHandler(h2)
	h2.setHandler(h3)
	
	request = [2, 5, 14, 22, 18, 3, 27, 20]
	
	for req in request:
		h1.handleRequest(req)