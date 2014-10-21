class OperationFactory:
    @staticmethod
    def createOperate(operate):
        if operate == '+':
            op = OperationAdd()
        elif operate == '-':
            op = OperationSub()
        elif operate == '*':
            op = OperationMul()
        else:
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
    op = OperationFactory.createOperate('/')
    op.numberA = 3
    op.numberB = 5
    res = op.getResult()
    print(res)
