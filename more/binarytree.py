class TreeNode:

# Init

    def __init__(self, val):
        self.rChild = None
        self.lChild = None
        self.value = val

# Getters

    def getleft(self):
        return self.lChild.value

    def getright(self):
        return self.rChild.value

    def getvalue(self):
        return self.value

# Setters

    def setvalue(self, val):
        self.value = val
        return True

    def addleft(self, val):
        self.lChild.value = val
        return True

    def addright(self, val):
        self.rChild.value = val
        return True

    def print(self):
        return str(self.value)+":"+str(self.lChild)+":"+str(self.rChild)

# Tree

class BinaryTree():
    # Initial

    def __init__(self):
        self.head = None
        self.size = 0
        # starts with no head
         
    def addRootNode(self, root):
        self.head = TreeNode(root)
        self.size = 1
        # makes head a tree node

    # Add Node

    def rca(self, node, val):
        if val > node.value:
            if node.rChild:
                return self.rca(node.rChild, val)
            else:
                node.rChild = TreeNode(val)
                return True
            # if the child is > parent then right
        else:
            if node.lChild:
                return self.rca(node.lChild, val)
            else:
                node.lChild = TreeNode(val)
                return True
    
    def addNode(self, val):
        self.rca(self.head, val)

        self.size += 1
        # size increased

    # Print Node
    
    def tr(self, node):
        x = []
        x.append(node.value)

        if node.lChild:
            x += [self.tr(node.lChild)]
        if node.rChild:
            x += [self.tr(node.rChild)]
        elif not node.lChild and not node.rChild:
            return x

        return x

    def print(self):
        return self.tr(self.head)

    # Delete
    def rcd(self, temp, val):
        x = []

        #CHECKS
        if not temp.lChild and not temp.rChild:
            return False
        elif temp.lChild and temp.lChild.value == val:
            # DECLARE
            tChild = temp.lChild
            # NO CHILDREN
            if not tChild.lChild and not tChild.rChild:
                temp.lChild = None
                return True
            # BOTH CHILDREN
            elif tChild.lChild and tChild.rChild:
                cTemp = temp
                cTemp = cTemp.lChild.lChild
                pTemp = temp
                pTemp = temp.lChild.lChild
                bool = False
                while cTemp.rChild:
                    cTemp = cTemp.rChild
                    if bool:
                        pTemp = pTemp.rChild
                    else:
                        bool = True
                        
                temp.lChild.value = cTemp.value
                if cTemp.lChild:
                    cTemp = cTemp.lChild
                else:
                    pTemp.rChild = None

                return True
            # LEFT CHILD ONLY
            elif tChild.lChild:
                temp.lChild = temp.lChild.lChild
                return True
            # RIGHT CHILD ONLY
            elif tChild.rChild:
                temp.lChild = temp.lChild.rChild
                return True
            return False 
        elif temp.rChild and temp.rChild.value == val:
            # DECLARE
            tChild = temp.rChild
            # NO CHILDREN
            if not tChild.lChild and not tChild.rChild:
                temp.rChild = None
                return True
            # BOTH CHILDREN
            elif tChild.lChild and tChild.rChild:
                cTemp = temp
                cTemp = cTemp.rChild.lChild
                pTemp = temp
                pTemp = temp.rChild.lChild
                bool = False
                while cTemp.rChild:
                    cTemp = cTemp.rChild
                    if bool:
                        pTemp = pTemp.rChild
                    else:
                        bool = True
                        
                temp.rChild.value = cTemp.value
                if cTemp.lChild:
                    cTemp = cTemp.lChild
                else:
                    pTemp.rChild = None

                return True
            # LEFT CHILD ONLY
            elif tChild.lChild:
                temp.rChild = temp.rChild.lChild
                return True
            # RIGHT CHILD ONLY
            elif tChild.rChild:
                temp.rChild = temp.rChild.rChild
                return True
            return False 
        elif temp.lChild:
            x.append(self.rcd(temp.lChild, val))
            if temp.rChild:
                x.append(self.rcd(temp.rChild, val))
            return(x)

    def deleteNode(self, val):
        # Declaration
        temp = self.head

        # Head is deleted (complicated case)
        if temp.value == val:
            cTemp = temp
            cTemp = cTemp.lChild
            pTemp = temp
            pTemp = temp.lChild
            bool = False
            while cTemp.rChild:
                cTemp = cTemp.rChild
                if bool:
                    pTemp = pTemp.rChild
                else:
                    bool = True
            temp.value = cTemp.value
            if cTemp.lChild:
                cTemp = cTemp.lChild
            else:
                pTemp.rChild = None

            return True

        # Recursion
        self.rcd(self.head, val)
        
# Testing

bTree = BinaryTree()
bTree.addRootNode(10)
bTree.addNode(5)
bTree.addNode(3)
bTree.addNode(7)
bTree.addNode(2)
bTree.addNode(4)
bTree.addNode(6)
bTree.addNode(8)
bTree.addNode(16)
bTree.addNode(18)
bTree.addNode(17)
bTree.addNode(20)
bTree.addNode(14)
bTree.addNode(12)
bTree.addNode(15)
bTree.deleteNode(10)
print(bTree.print())