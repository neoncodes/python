from asyncio.windows_events import NULL
from re import L

from regex import R


class TreeNode:

# Init

    def __init__(self, val):
        self.rchild = NULL
        self.lchild = NULL
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