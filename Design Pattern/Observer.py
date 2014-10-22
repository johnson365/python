"""Implementation of Observer pattern"""
from abc import ABCMeta, abstractmethod

class Subject:
    """The abstract class of Subject put all Observer object in a collection!"""
    
    def __init__(self):
        self.observers = []
        
    def attachObserver(self, observer):
        """add a observer into observer collection"""
        self.observers.append(observer)
        
    def removeObserver(self, observer):
        """remove a observer from observer collection"""
        self.observers.remove(observer)
        
    def notify(self):
        """notify all observers when state changed"""
        for ob in self.observers:
            ob.updateState()
            
class Observer:
    """The abstract class of Observer"""
    __metaclass__ = ABCMeta
    
    @abstractmethod
    def updateState(self):pass
    
class ConcreteSubject(Subject):
    """The concrete class of subject"""
    def __init__(self):
        Subject.__init__(self)
        self.__subjectState = None
    
    def getSubjectState(self):
        return self.__subjectState
        
    def setSubjectState(self, state):
        self.__subjectState = state
        
class ConcreteObserver(Observer):
    """ The concrete class of Observer"""
    def __init__(self, subject, name):
        self.__subject = subject
        self.__name = name
        self.__state = None
        
    def getSubject(self):
        return self.__subject
        
    def setSubject(self, subject):
        self.__subject = subject
        
    def updateState(self):
		"""update state by subject`s state"""
        self.__state = self.__subject.getSubjectState()
        print "Observer%s `s new state is %s" % (self.__name, self.__state)
        
if __name__ == '__main__':
    s = ConcreteSubject()
    x = ConcreteObserver(s, 'x')
    y = ConcreteObserver(s, 'Y')
    z = ConcreteObserver(s, 'z')
    s.attachObserver(x)
    s.attachObserver(y)
    s.attachObserver(z)
    s.setSubjectState("ABC")
    s.notify()
