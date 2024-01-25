class Node:
    def __init__(self, key, left = None, right = None):
        self.left = left
        self.right = right
        self.key = key

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
                putta(root.right, newkey)
        
        return root



def finns(root, key):
    if root == None:
        return False
    
    if key == root.key:
        return True
    
    if key > root.key:
        return finns(root.right, key)
    
    if key < root.key:
        return finns(root.left, key)
   
    else:
        raise ValueError('An error has occured')


def skriv(root):
    if root is not None:
        skriv(root.left)
        print(root.key)
        skriv(root.right)