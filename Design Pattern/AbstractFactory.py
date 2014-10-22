"""Implementation of Abstract Factory pattern"""
from abc import ABCMeta, abstractmethod

class AUser:
	"""The abstract class of User"""
	__metaclass__ = ABCMeta
	
	@abstractmethod
	def insertUser(self, user):pass
	@abstractmethod
	def getUser(self, id):pass
	
class SqlserverUser(AUser):
	"""User class of Sqlserver database"""
	
	def insertUser(self, user):
		print "insert a record in user table in database sqlserver"
		
	def getUser(self, id):
		print "query a record by id from user table in database sqlserver"
		
class AccessUser(AUser):
	"""User class of Access database"""
	
	def insertUser(self, user):
		print "insert a record in user table in database Access"
		
	def getUser(self, id):
		print "query a record by id from user table in database Access"	

class ADepartment:
	"""The abstract class of Department"""
	__metaclass__ = ABCMeta
	
	@abstractmethod
	def insertDep(self, dep):pass
	@abstractmethod
	def getDepartment(self, id):pass
	
class SqlserverDepartment(ADepartment):
	"""Department class of Sqlserver database"""
	
	def insertDep(self, dep):
		print "insert a record in department table in database sqlserver"
		
	def getDepartment(self, id):
		print "query a record by id from department table in database sqlserver"
		
class AccessDepartment(ADepartment):
	"""Department class of Access database"""
	
	def insertDep(self, dep):
		print "insert a record in department table in database Access"
		
	def getDepartment(self, id):
		print "query a record by id from department table in database Access"
		
class AFactory:
	"""The abstract class of Factory"""
	
	__metaclass__ = ABCMeta
	
	@abstractmethod
	def createUser(self):pass
	@abstractmethod
	def createDepartment(self):pass
	
class SqlserverFactory(AFactory):
	"""Factory class of Sqlserver database"""
	
	def createUser(self):
		return SqlserverUser()
	
	def createDepartment(self):
		return SqlserverDepartment()
		
class AccessFactory(AFactory):
	"""Factory class of Access database"""
	
	def createUser(self):
		return AccessUser()
	
	def createDepartment(self):
		return AccessDepartment()
		
if __name__ == '__main__':
	fac = AccessFactory()
	
	iu = fac.createUser()
	iu.insertUser('user')
	iu.getUser(1)
	
	id = fac.createDepartment()
	id.insertDep('dep')
	id.getDepartment(1)
	