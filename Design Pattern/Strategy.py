from abc import ABCMeta, abstractmethod

class Strategy:
	__metaclass__ = ABCMeta
	
	@abstractmethod
	def algorithmInterface(self):
		pass
		
class ConcreteStrategyA(Strategy):

	def algorithmInterface(self):
		print('Implementation of Algorithm A!')
		
class ConcreteStrategyB(Strategy):

	def algorithmInterface(self):
		print('Implementation of Algorithm B!')
		
class ConcreteStrategyC(Strategy):

	def algorithmInterface(self):
		print('Implementation of Algorithm C!')
		
class Context:
	
	def __init__(self, strategy):
		self.strategy = strategy
	
	def contextInterface(self):
		self.strategy.algorithmInterface()
		
if __name__ == '__main__':
	context = Context(ConcreteStrategyA())
	context.contextInterface()
	
	context = Context(ConcreteStrategyB())
	context.contextInterface()
	
	context = Context(ConcreteStrategyC())
	context.contextInterface()