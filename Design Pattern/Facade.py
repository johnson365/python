"""Implementation of Facade pattern"""
from abc import ABCMeta, abstractmethod

class SubsystemOne:
	
	def methodOne(self):
		print('SubsystemOne`s methodOne!')
		
class SubsystemTwo:
	
	def methodTwo(self):
		print('SubsystemTwo`s methodTwo!')
		
class SubsystemThree:
	
	def methodThree(self):
		print('SubsystemThree`s methodThree!')
		
class SubsystemFour:
	
	def methodFour(self):
		print('SubsystemFour`s methodFour!')
		
class Facade:

	def __init__(self):
		self._one = SubsystemOne()
		self._two = SubsystemTwo()
		self._three = SubsystemThree()
		self._four = SubsystemFour()
		
	def methodA(self):
		print('Method group A...')
		self._one.methodOne()
		self._two.methodTwo()
		self._three.methodThree()
	
	def methodB(self):
		print('Method group B...')
		self._three.methodThree()
		self._two.methodTwo()
		
if __name__ == '__main__':
	f = Facade()
	f.methodA()
	f.methodB()
		
