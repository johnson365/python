from abc import ABCMeta, abstractmethod

class Subject:

	__metaclass__ = ABCMeta
	
	@abstractmethod
	def request(self):pass
	
class RealSubject(Subject):
	
	def request(self):
		print('The real request of subject!')
		
class Proxy(Subject):
	
	def __init__(self):
		self.__realSubject = None

	def request(self):
		if self.__realSubject == None:
			self.__realSubject = RealSubject()
		self.__realSubject.request()
		
if __name__ == '__main__':
	proxy = Proxy()
	proxy.request()