class Node:
    def __init__(self, value, nextNode):
        self.value = value
        self.nextNode = nextNode

class LinkedList:
    def __init__(self, head):
        self.head = Node(head, None)

    def append(self, value):
        temp = self.head
        while temp.nextNode != None:
            temp = temp.nextNode
        temp.nextNode = Node(value, None)
        return True

    # Returning Functions (print, size)

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

    # Removal Functions
    
    def remove(self, val):
        temp = self.head
        while temp.nextNode != None:
            if temp.nextNode.value == val:
                if temp.nextNode.nextNode:
                    temp.nextNode = temp.nextNode.nextNode
                else:
                    temp.nextNode = None
                return True
            temp = temp.nextNode
        return False

    def pop(self, ind):
        temp = self.head
        cInd = 0
        while temp.nextNode != None:
            if cInd == ind-1:
                if temp.nextNode.nextNode:
                    temp.nextNode = temp.nextNode.nextNode
                else:
                    temp.nextNode = None
                return True
            temp = temp.nextNode
            cInd = cInd + 1
        return False

lList = LinkedList("A")
lList.append("B")
lList.append("C")
lList.append("D")
lList.append("E")
lList.append("F")
lList.remove("D")
lList.pop(4)
print(lList.size())
print(lList.print())
