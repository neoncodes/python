class Node:
    def __init__(self, value, nextNode):
        self.value = value
        self.nextNode = nextNode
class Stack:
    def __init__(self, head):
        self.head = Node(head, None)

    # Pop/Push

    def pop(self):
        temp = self.head
        temp = temp.nextNode
        
        return True
        
    def push(self, val):
        temp = self.head
        if temp.nextNode:
            self.head.nextNode = Node(temp.value, temp.nextNode)
            self.head.value = val
        else:
            self.head.nextNode = Node(temp.value, None)
            self.head.value = val

        return True
            

    # Print/Size

    def print(self):
        temp = self.head
        string = str(temp.value)
        while temp.nextNode != None:
            temp = temp.nextNode
            string += ", "+str(temp.value)
        return string

    def size(self):
        temp = self.head
        s = 1
        while temp.nextNode != None:
            s = s+1
            temp = temp.nextNode
        return s

lStack = Stack("A")
lStack.push("B")
lStack.push("C")
print(lStack.print())
print(lStack.size())