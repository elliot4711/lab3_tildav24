from bintreeFile import Bintree

def makeTree():
    """
    Function to make a binomial tree with input values from user
    Parameters: None
    Returns: None
    """

    tree = Bintree()
    data = input().strip()
    while data != "#":
        tree.put(data)
        data = input().strip()
    return tree

def searches(tree):
    """
    Function to search for value of user input in binomial tree
    Parameters: tree to search in
    Returns: None
    """

    findme = input().strip()
    while findme != "#":
        if findme in tree:
            print(findme, "found")
        else:
            print(findme, "not found")
        findme = input().strip()


def main():
    """
    Main function to run program
    Parameters: None
    Returns: None
    """

    tree = makeTree()
    searches(tree)
    print("\n")
    tree.write()
    print("\n")
    tree.writepostorder()
    print("\n")
    tree.writepreorder()

main()