
class Nilnode(object):
    def __init__(self):
        self.color = "black"

class Tree(object):
    def __init__(self,c, root=None):
        self.root = root
        self.c = c

class Node(object):
    def __init__(self, key, color="red", left=None, right=None, p=None):
        self.color = color
        self.key = key
        self.left = left
        self.right = right
        self.p = p

class counter(object):
    def __init__(self,count=0):
        self.count = count
    def increment(self):
        self.count+=1
    def reset(self):
        self.count = 0
    def query(self):
        return self.count
