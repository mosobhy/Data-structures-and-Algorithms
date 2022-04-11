# this file is based on the Tree data structure of tree.py

def printLeafNodes(root):
    if root == None:
        return
    # the base case for leaf nodes
    if root.left == None and root.right == None:
        print(root.data)

    if root.left != None:
        printLeafNodes(root.left)

    if root.right != None:
        printLeafNodes(root.right)



