class Node:
    def __init__(self, value, nextNode):
        self.value = value
        self.nextNode = nextNode
class Queue:
    def __init__(self, head):
        self.head = Node(head, None)

    # Pop/Push

    def delete(self):
        self.head = self.head.nextNode
        
        return True
        
    def add(self, val):
        temp = self.head
        if temp.nextNode:
            while temp.nextNode:
                temp = temp.nextNode
            temp.nextNode = Node(val, None)
        else:
            self.head.nextNode = Node(val, None)

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

lStack = Queue("A")
lStack.add("B")
lStack.add("C")
lStack.delete()
print(lStack.print())
print(lStack.size())