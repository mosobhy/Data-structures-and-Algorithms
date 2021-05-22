'''
for building a parse tree we will follow these rules

1. break the expression into a list of tokens ['(', '+', '4' ..]
2. iterate over this list and check if the token is '(', add a new node as the left child
    of the current node and descend to the left child
3. if the current token is an operator [+, -, *, /], set the current value of the root node
    to the operator presented by the current token... add new node as the right child of the
    current node and descend to the right child
4. if the current token is a number, set the root value of the current node to the number
    and return to the parent
5. if the current token is ')', go to the parent of the current node

So how we gonna keep track of the parent node?
    via using a Stack object,,, everytime we want oto descend to a child of the current node
    ====> we first push the current node to the Stack
    when we want to retrun to the parent of the current node ====> we pop the parent of
    the Stack

'''
# building the Tree class that gonna support the parse tree
class BinaryTree:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def insertLeft(self, val):
        if self.left == None:
            self.left = BinaryTree(val)
        else:
            #traverse
            self.left.insertLeft(val)
    
    def insertRight(self, val):
        if self.right == None:
            self.right = BinaryTree(val)
        else:
            self.right.insertRight(val)
    
    def setCurrentVal(self, val):
        self.data = val

    def getLeftChild(self):
        return self.left
    
    def getRightChild(self):
        return self.right

    def getCurrentVal(self):
        return self.data

    def InOrderTraversal(self):
        if self.left is not None:
            self.left.InOrderTraversal()

        print(self.data)

        if self.right is not None:
            self.right.InOrderTraversal()

#################################################################

def buildParseTree(exp):
    ''' we have to follow the 4 rules of expression '''
    tokens = exp.split(' ')
    parse_tree = BinaryTree('')
    parent_stack = []       # to keep track of the parents
    parent_stack.append(parse_tree)     # push the root of the tree
    current = parse_tree

    for token in tokens:
        if token == '(':
            # create a left child and proceed to it
            current.insertLeft('')
            parent_stack.append(current)

            current = current.getLeftChild()
        
        elif token not in ['+', '-', '*', '/'] and token != ')':
            # numeric token
            # set the value of the current node to this token
            current.setCurrentVal(int(token))

            # pop this node of the stack...(means get back to the parent)
            current = parent_stack.pop()

        elif token in ['+', '-', '*', '/']:
            # set current node value to this operator
            current.setCurrentVal(token)

            # create a new right child and proceed to it
            current.insertRight('')
            parent_stack.append(current)

            current = current.getRightChild()

        elif token == ')':
            # get back to the parent
            current = parent_stack.pop()
        
        else:
            # not valid token
            raise ValueError
        
    return parse_tree

##################################################################

if __name__ == "__main__":

    expression1 = "( 3 * ( 4 + 5 ) )"
    expression2 = "( ( 7 + 3 ) * ( 5 - 2 ) )"
    parse_tree1 = buildParseTree(expression1)
    parse_tree2 = buildParseTree(expression2)

    parse_tree1.InOrderTraversal()
    print()
    parse_tree2.InOrderTraversal()

