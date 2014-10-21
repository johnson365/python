from abc import ABCMeta, abstractmethod

class Component:
	
	__metaclass__ = ABCMeta
	@abstractmethod
	def operation(self):
		pass
		
class ConcreteComponent(Component):
	
	def operation(self):
		print('The operation of concrete component!')
		
class Decorator(Component):
	
	def setComponent(self, component):
		self.component = component
		
	def operation(self):
		if self.component != None:
			self.component.operation()
			
			
class ConcreteDecoratorA(Decorator):
	
	def operation(self):
		self.component.operation()
		self.__addedState = 'new State'
		print('Implementation of concrete decorator A!')
		
class ConcreteDecoratorB(Decorator):
	
	def operation(self):
		self.component.operation()
		self.__addedBehavior()
		print('Implementation of concrete decorator B!')
		
	def __addedBehavior(self):
		print('self.__addedBehavior()')
		
if __name__ == '__main__':
        
	c = ConcreteComponent()
	d1 = ConcreteDecoratorA()
	d2 = ConcreteDecoratorB()
	
	d1.setComponent(c)
	d2.setComponent(d1)
	d2.operation()
	
