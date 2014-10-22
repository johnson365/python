"""Implementation of Adapter pattern"""
from abc import ABCMeta, abstractmethod

class Player:
    """ The abstract class of Player"""
    def __init__(self, name):
        self._name = name
        
    @abstractmethod
    def attack(self):pass
    @abstractmethod
    def defense(self):pass
    
class Forwards(Player):
    """The class of basketball forward player"""
    def __init__(self, name):
        Player.__init__(self,name)
        
    def attack(self):
        print "Forward %s attack!" % (self._name)
    
    def defense(self):
        print "Forward %s defense!" % (self._name)
        
class Center(Player):
    """The class of basketball center player"""
    def __init__(self, name):
        Player.__init__(self,name)
        
    def attack(self):
        print "Center %s attack!" % (self._name)
    
    def defense(self):
        print "Center %s defense!" % (self._name)
        
class Guards(Player):
    """The class of basketball guard player"""
    def __init__(self, name):
        Player.__init__(self,name)
        
    def attack(self):
        print "Guards %s attack!" % (self._name)
    
    def defense(self):
        print "Guards %s defense!" % (self._name)
        
class ForeignCenter:
    """ The class of basketball foreign center player """
    def __init__(self, name):
        self.__name = name
    
    def setName(self, name):
        self.__name = name
    
    def getName(self):
        return self.__name
        
    def foreignAttack(self):
        print "Foreign center %s attack!" % (self.__name)
        
    def foreignDefense(self):
        print "Foreign center %s defense!" % (self.__name)
        
class Translator(Player):
    """The class of basketball player`s translator"""
    def __init__(self, name):
        Player.__init__(self,name)
        self.__fc = ForeignCenter(name)
        
    def attack(self):
        self.__fc.foreignAttack()
    
    def defense(self):
        self.__fc.foreignDefense()
        
        
if __name__ == '__main__':
    
    b = Forwards('gay')
    b.attack()
    k = Guards('kobe')
    k.attack()
    y = Translator('yao')
    y.attack()
    y.defense()
    
