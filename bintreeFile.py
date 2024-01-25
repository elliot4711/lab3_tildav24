class Node:
    def __init__(self, key, left = None, right = None, parent = None):
        self.left = left
        self.right = right
        self.key = key
        self.parent = parent

class Bintree:
    def __init__(self):
        self.root = None
        self.size = 0
    
    def length(self):
        return self.size

    def __len__(self):
        return self.size

    def put(self,newvalue):
        # Sorterar in newvalue i trädet
        self.root = putta(self.root,newvalue)

    def __contains__(self,value):
        # True om value finns i trädet, False annars
        return finns(self.root,value)

    def write(self):
        # Skriver ut trädet i inorder
        skriv(self.root)
        print("\n")

    def putta(self):


    def finns(self):


    def skriv(self):