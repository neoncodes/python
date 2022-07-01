from xml.dom import IndexSizeErr
from regex import R


class Stack:
    def __init__(self, m):
        self.list = [None]*2**m
        self.topVal = -1
        self.max = 2**m

    def push(self, val):
        self.topVal += 1
        if self.topVal == self.max:
            raise IndexError
        self.list[self.topVal] = val

        return True
        

    def pop(self):
        x = self.list[self.topVal]

        self.list[self.topVal] = None
        self.topVal -= 1

        return x
    
    def peak(self):
        return self.list[self.topVal]
    
    def print(self):
        return self.list

stackTest = Stack(3)
stackTest.push(3)
stackTest.push(13)
stackTest.push(32)
stackTest.push(33)
stackTest.push(34)
stackTest.pop()
print(stackTest.peak())
print(stackTest.print())


    

