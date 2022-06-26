class TreeNode:

# Init

    def __init__(self, val):
        self.rchild = None
        self.lchild = None
        self.value = val

# Getters

    def getleft(self):
        return self.lchild

    def getright(self):
        return self.rchild

    def getvalue(self):
        return self.value

# Setters

    def setvalue(self, val):
        self.value = val
        return True

    def addleft(self, val):
        self.lchild = val
        return True

    def addright(self, val):
        self.rchild = val
        return True

    def print(self):
        return str(self.value)+":"+str(self.lchild)+":"+str(self.rchild)

# Tree

class BinaryTree():
    def __init__(self):
        self.head = None
        self.size = 0
        # starts with no head
         
    def addRootNode(self, root):
        self.head = TreeNode(root)
        self.size = 1
        # makes head a tree node

    def addNode(self, node, val):
        if val > node.value:
            node.rchild = val
            # if the child is > parent then right
        else:
            node.lchild = val
            # else left

        self.size += 1
        # size increased

    def print(self):
        # for tmr