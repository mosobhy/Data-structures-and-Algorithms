'''
A tree data strcuture looks like a real tree but it just has its root at
the top...
There are multiple ways to implement a tree data structure in python
1. List of Lists Representation
2. Node and Reference Representaion

so here in this file, i am going to implement the tree using the second approach.
'''

# the tree will be a collection of Node instances connected together via left and right references
class Node:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    
    def insert(self, value):
        # get to the appropriate position to insert the node
        if value <= self.data:
            if self.left == None:
                self.left = Node(value)
            else:
                self.left.insert(value)
        else:
            if self.right == None:
                self.right = Node(value)
            else:
                self.right.insert(value)

    def contains(self, value):
        # return True of a value is found in the binary tree
        if value == self.data:      # found
            return True
        else:
            if value < self.data:   # search in left
                if self.left is None:
                    return False
                else: 
                    return self.left.contains(value)
            
            else:                   # search in the right
                if self.right is None:
                    return False
                else:
                    return self.right.contains(value)
    
    def deleletValue(self, value):
        pass

    def preOrderTraversal(self):
        # in this algorithm we visit root then left subtree then right subtree
        print(self.data)
        if self.left is not None:
            self.left.preOrderTraversal()
        if self.right is not None:
            self.right.preOrderTraversal()

    def inOrderTraversal(self):
        # in this traverse algorithm, we first traverse the left subtree, then visit the root
        # and lastly the right subtree
        if self.left is not None:
            self.left.inOrderTraversal()
        print(self.data)
        if self.right is not None:
            self.right.inOrderTraversal()

    def postOrderTraversal(self):
        # in this traverse alogrithm, we first traverse the left subtree then the right subtree
        # and lastly we visit the root node
        if self.left is not None:
            self.left.postOrderTraversal()
        if self.right is not None:
            self.right.postOrderTraversal()
        print(self.data)


if __name__ == '__main__':
    
    # tree instance
    tree = Node(88)
    tree.insert(4)
    tree.insert(16)
    tree.insert(5)
    tree.insert(0)
    tree.insert(9)
    tree.insert(1234)

    print("Pre-Order traversal")
    tree.preOrderTraversal()

    print('In-Order traversal')
    tree.inOrderTraversal()

    print('Post-Order traversal')
    tree.postOrderTraversal()

    print(tree.contains(0))
    print(tree.contains(16))
    print(tree.contains(-1))