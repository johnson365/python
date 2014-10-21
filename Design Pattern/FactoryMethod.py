from abc import ABCMeta, abstractmethod

class IFactory:

    __metaclass__ = ABCMeta
    
    @abstractmethod
    def createOperation(self):
        pass

class AddFactory(IFactory):

    def createOperation(self):
        op = OperationAdd()
        return op
        
class SubFactory(IFactory):

    def createOperation(self):
        op = OperationSub()
        return op
        
class MulFactory(IFactory):

    def createOperation(self):
        op = OperationMul()
        return op
        
class DivFactory(IFactory):

    def createOperation(self):
        op = OperationDiv()
        return op
        
class Operation:
    def getResult(self):
        res = 0
        return res
        
class OperationAdd(Operation):
    def getResult(self):
        res = 0
        res = self.numberA + self.numberB
        return res
        
class OperationSub(Operation):
    def getResult(self):
        res = 0
        res = self.numberA - self.numberB
        return res
        
class OperationMul(Operation):
    def getResult(self):
        res = 0
        res = self.numberA * self.numberB
        return res
        
class OperationDiv(Operation):
    def getResult(self):
        res = 0
        res = self.numberA / self.numberB
        return res
        
if __name__ == '__main__':
    opf = AddFactory()
    op = opf.createOperation()
    op.numberA = 3
    op.numberB = 5
    res = op.getResult()
    print(res)
