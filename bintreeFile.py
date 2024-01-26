class Node:
    def __init__(self, key, left = None, right = None):
        self.left = left
        self.right = right
        self.key = key

"""
För att testa Bintree kan man använda enkla siffror och se om dem placeras rätt (större till höger)
"""

class Bintree:
    def __init__(self):
        self.root = None
    
    #def length(self):
        #return self.size

    #def __len__(self):
        #return self.size

    def __contains__(self,key):
        # True om key finns i trädet, False annars
        return finns(self.root, key)
    
    def put(self,newkey):
        # Sorterar in newkey i trädet
        self.root = putta(self.root, newkey)

    def write(self):
        # Skriver ut trädet i inorder
        skriv(self.root)
        print("\n")


def putta(root, newkey):
    
    if root == None:
        return Node(newkey)
    
    else:
        if newkey > root.key:
            if root.right == None:
                root.right = Node(newkey)
            
            else:
                putta(root.right, newkey)
        
        else:
            if root.left == None:
                root.left = Node(newkey)
            
            else:
                putta(root.left, newkey)
        
        return root



def finns(root, searched):
    if root == None:
        #print("1")
        return False
    
    #print(root.key)
    #print(searched)
    
    if searched == root.key:
        #print("2")
        return True
    
    if searched > root.key:
        #print("3")
        return finns(root.right, searched)
    
    if searched < root.key:
        #print("4")
        return finns(root.left, searched)
   
    else:
        raise ValueError('An error has occured')
    
    


def skriv(root):
    if root is not None:
        skriv(root.left)
        print(root.key)
        skriv(root.right)