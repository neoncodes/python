from lib2to3.pytree import Node
from re import I


class avlNode:

# Init

    def __init__(self, val, parent):
        self.rChild = None
        self.lChild = None
        self.bal = 0
        self.parent = parent
        self.value = val
        self.height = 1

class avlTree:

    def __init__(self, val):
        self.head = avlNode(val, None)
    
    def lRotate(self, node):
        if node.lChild:
            y = node.parent
            x = node.lChild
            if node.rChild:
                return False
            elif node == self.head:
                node.lChild = None
                self.head = x
                x.rChild = node
                node.parent = x
                x.parent = None
                print(x.value)
                node = self.head
                while node.rChild:
                    if not node.rChild:
                        self.aHeight(node)
                    else:
                        node = node.rChild
                node = self.head
                while node.lChild:
                    if not node.lChild:
                        return self.aHeight(node)
                    else:
                        node = node.lChild
            elif node.parent.lChild == node:
                y.lChild = x
                node.lChild = None
                x.rChild = node
                node.parent = x
                x.parent = y
                node = self.head
                while node.rChild:
                    if not node.rChild:
                        self.aHeight(node)
                    else:
                        node = node.rChild
                node = self.head    
                while node.lChild:
                    if not node.lChild:
                        return self.aHeight(node)
                    else:
                        node = node.lChild
            else:
                y.rChild = x
                node.lChild = None
                x.rChild = node
                node.parent = x
                x.parent = y

                node = self.head
                while node.rChild:
                    if not node.rChild:
                        self.aHeight(node)
                    else:
                        node = node.rChild
                
                node = self.head
                while node.lChild:
                    if not node.lChild:
                        return self.aHeight(node)
                    else:
                        node = node.lChild

            return True
        else:
            return False

    #def lrRotate(self):

    def rRotate(self, node):
        if node.rChild:
            y = node.parent
            x = node.rChild
            if node.lChild:
                return False
            elif node == self.head:
                node.rChild = None
                self.head = x
                x.lChild = node
                node.parent = x
                x.parent = None
                node = self.head
                while node.rChild:
                    if not node.rChild:
                        self.aHeight(node)
                    else:
                        node = node.rChild
                node = self.head
                while node.lChild:
                    if not node.lChild:
                        return self.aHeight(node)
                    else:
                        node = node.lChild
            elif node.parent.lChild == node:
                y.lChild = x
                node.rChild = None
                x.lChild = node
                node.parent = x
                x.parent = y

                node = self.head
                while node.rChild:
                    if not node.rChild:
                        self.aHeight(node)
                    else:
                        node = node.rChild
                node = self.head
                while node.lChild:
                    if not node.lChild:
                        return self.aHeight(node)
                    else:
                        node = node.lChild
            else:
                y.rChild = x
                node.rChild = None
                x.lChild = node
                node.parent = x
                x.parent = y
                
                node = self.head
                while node.rChild:
                    if not node.rChild:
                        self.aHeight(node)
                    else:
                        node = node.rChild
                
                node = self.head
                while node.lChild:
                    if not node.lChild:
                        return self.aHeight(node)
                    else:
                        node = node.lChild
                
            return True
        else:
            return False
    # ADD FUNCTION
    # def balance(self, newNode):
    #     if newNode:
    #         if newNode.lChild and newNode.rChild:
    #             newNode.bal = newNode.lChild.height - newNode.rChild.height
    #         elif newNode.lChild:
    #             newNode.bal = newNode.lChild.height
    #         elif newNode.rChild:
    #             newNode.bal = 0 - abs(newNode.rChild.height)
    #         else:
    #             newNode.bal = 0

    #         if newNode.bal < -1:
    #             self.rRotate(newNode)  
    #         if newNode.bal > 1:
    #             self.lRotate(newNode) 

    def aHeight(self, newNode):
        if not newNode:
            return False
        else:
            print(newNode.value)
            if newNode.lChild and newNode.rChild:
                if newNode.height == 0 or newNode.height == newNode.lChild.height:
                    newNode.height += 1  
                if newNode.height == 0 or newNode.height == newNode.rChild.height:
                    newNode.height += 1  
                newNode.bal = newNode.lChild.height - newNode.rChild.height
            elif newNode.lChild:
                if newNode.height == 0 or newNode.height == newNode.lChild.height:
                    newNode.height += 1  
                newNode.bal = newNode.lChild.height
            elif newNode.rChild:
                if newNode.height == 0 or newNode.height == newNode.rChild.height:
                    newNode.height += 1 
                newNode.bal = 0 - abs(newNode.rChild.height)
            else:
                newNode.height = 1

            if newNode.bal < -1:
                self.rRotate(newNode)  
            if newNode.bal > 1:
                self.lRotate(newNode)  

            if newNode.parent:
                return self.aHeight(newNode.parent)
            return True

    def adder(self, node, val):
        if val > node.value:
            if node.rChild:
                return self.adder(node.rChild, val)
            else:
                node.rChild = avlNode(val, node)
                self.aHeight(node)
                return True
            # if the child is > parent then right
        else:
            if node.lChild:
                return self.adder(node.lChild, val)
            else:
                node.lChild = avlNode(val, node)
                self.aHeight(node)
                return True
    
    def addNode(self, val):
        self.adder(self.head, val)

    # REMOVE FUNCTION
    
    # PRINT FUNCTION

    def tr(self, node):
        x = []
        x.append(str(node.value)+":"+str(node.bal))

        if node.lChild:
            x += [self.tr(node.lChild)]
        if node.rChild:
            x += [self.tr(node.rChild)]
        elif not node.lChild and not node.rChild:
            return x

        return x

    def print(self):
        return self.tr(self.head)



# TESTING
coolTree = avlTree(1)
coolTree.addNode(0)
coolTree.addNode(-1)
coolTree.addNode(-2)
# coolTree.addNode(5)
# coolTree.addNode(3)
# coolTree.addNode(12)
# coolTree.addNode(16)
# coolTree.addNode(8)
# coolTree.addNode(2134234)
# coolTree.addNode(13)
# coolTree.addNode(1)
# coolTree.addNode(0)
# coolTree.addNode(-1)
# coolTree.addNode(-2)
# coolTree.addNode(34324)
# coolTree.addNode(214234)
# coolTree.addNode(1453)
print(coolTree.print())

