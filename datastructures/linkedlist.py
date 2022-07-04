class Node:
    def __init__(self, value, nextNode):
        self.value = value
        self.nextNode = nextNode


class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0
        self.tail = None

    def append(self, value):
        if not self.head:
            self.head = Node(value, None)
            self.tail = self.head
        else:
            self.tail.nextNode = Node(value, None)
            self.tail = self.tail.nextNode
        self.size += 1

    # Returning Functions (print, size)

    def __repr__(self):
        temp = self.head
        string = str(temp.value)
        while temp.nextNode:
            temp = temp.nextNode
            string += ", " + str(temp.value)
        return f"<{string}>"

    def size(self):
        return self.size

    # Removal Functions

    def remove(self, val):
        temp = self.head
        x = 0
        if not temp:
            return False
        if temp.value == val:
            self.head = self.head.nextNode
        while temp.nextNode:
            if temp.nextNode.value == val:
                if temp.nextNode.nextNode:
                    temp.nextNode = temp.nextNode.nextNode
                else:
                    temp.nextNode = None
                return True
            x += 1
            temp = temp.nextNode
        self.size -= 1
        return x
    def pop(self, y):
        temp = self.head
        x = 0
        while temp.nextNode:
            if x == y - 1:
                if temp.nextNode.nextNode:
                    temp.nextNode = temp.nextNode.nextNode
                else:
                    temp.nextNode = None
                return True
            temp = temp.nextNode
            x = x + 1
        self.size -= 1
        return False