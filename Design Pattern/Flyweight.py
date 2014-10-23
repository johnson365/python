"""Implementation of Chain of Flyweight pattern"""
from abc import ABCMeta, abstractmethod

class Flyweight(object):
    """ The abstract class of Flyweight """
    __metaclass__ = ABCMeta
    
    @abstractmethod
    def operation(self, ex):pass
    
class ConcreteFlyweight(Flyweight):
    """ The concrete class of Flyweight """
    
    def operation(self, ex):
        print "Concrete Flyweight:%s" % (ex)

class UnsharedConcreteFlyweight(Flyweight):
    """ The concrete class of do not need to share Flyweight """
    
    def operation(self, ex):
        print "no need to share concrete Flyweight:%s" % (ex)
        
class FlyweightFactory(object):
    """ The FlyweightFactory is a factory to create and manage Flyweight """
    
    def __init__(self):
        self.__flyweights = {}
        self.__flyweights['x'] = ConcreteFlyweight()
        self.__flyweights['y'] = ConcreteFlyweight()
        self.__flyweights['z'] = ConcreteFlyweight()

    def getFlyweight(self, key):
        return self.__flyweights[key]
        
if __name__ == '__main__':
    ex = 22
    ff = FlyweightFactory()
    
    fx = ff.getFlyweight('x')
    ex = ex - 1
    fx.operation(ex)
    
    fy = ff.getFlyweight('y')
    ex = ex - 1
    fy.operation(ex)
    
    fz = ff.getFlyweight('z')
    ex = ex - 1
    fz.operation(ex)
    
    uf = UnsharedConcreteFlyweight()
    ex = ex - 1
    uf.operation(ex)
