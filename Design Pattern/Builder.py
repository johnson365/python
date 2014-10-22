"""Implementation of Builder pattern"""
from abc import ABCMeta, abstractmethod

class PersonBuilder:
	""" The abstract Person builder class"""
		
	@abstractmethod
	def buildHead(self):pass
	@abstractmethod
	def buildBody(self):pass
	@abstractmethod
	def buildArmLeft(self):pass
	@abstractmethod
	def buildArmRight(self):pass
	@abstractmethod
	def buildLegLeft(self):pass
	@abstractmethod
	def buildLegRight(self):pass
	
class PersonThinBuilder(PersonBuilder):
	""" class of build thin person"""
	
	def buildHead(self):
		print('build thin person`s head!')
	
	def buildBody(self):
		print('build thin person`s body!')
		
	def buildArmLeft(self):
		print('build thin person`s left arm!')
		
	def buildArmRight(self):
		print('build thin person`s right arm!')
		
	def buildLegLeft(self):
		print('build thin person`s left leg!')
		
	def buildLegRight(self):
		print('build thin person`s right leg!')
		
class PersonFatBuilder(PersonBuilder):
	""" class of build thin person"""
	
	def buildHead(self):
		print('build fat person`s head!')
	
	def buildBody(self):
		print('build fat person`s body!')
		
	def buildArmLeft(self):
		print('build fat person`s left arm!')
		
	def buildArmRight(self):
		print('build fat person`s right arm!')
		
	def buildLegLeft(self):
		print('build fat person`s left leg!')
		
	def buildLegRight(self):
		print('build fat person`s right leg!')
	
class PersonDirector:
	"""class of director to control build person"""
	def __init__(self, pb):
		self.__pb = pb
	
	def createPerson(self):
		self.__pb.buildHead()
		self.__pb.buildBody()
		self.__pb.buildArmLeft()
		self.__pb.buildArmRight()
		self.__pb.buildLegLeft()
		self.__pb.buildLegRight()
		
if __name__ == '__main__':
	ptb = PersonThinBuilder()
	pdt = PersonDirector(ptb)
	pdt.createPerson()
	
	pfb = PersonFatBuilder()
	pdf = PersonDirector(pfb)
	pdf.createPerson()
	