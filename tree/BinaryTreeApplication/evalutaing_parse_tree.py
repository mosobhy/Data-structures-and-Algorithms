'''
evalutaing the parse tree means calculate its value
((7 * 3) + (5 + 4)) ===> 30

so we are going to implement this algorithm recursively dude
'''
from PraseTree import buildParseTree
import operator     # this module is going to provide us the functional version of the mathematical oprators

########################################################################

def evaluatePraseTree(p_tree):
    # map each operator to its function using dictionary
    operators = {
        '+': operator.add,   # the add is a function pointer  (not invoked yet)
        '-': operator.sub,
        '*': operator.mul,
        '/': operator.truediv
    }
    
    # the base case of this recursion will be the leaf nodes..
    # so the algorithms will move towards them
    left_subtree = p_tree.getLeftChild()
    right_subtree = p_tree.getRightChild()

    if left_subtree and right_subtree:
        func = operators[p_tree.getCurrentVal()]     # get the operator type

        left_evalutate = evaluatePraseTree(left_subtree)
        right_evalutate = evaluatePraseTree(right_subtree)

        return func(left_evalutate, right_evalutate)

    else:
        return p_tree.getCurrentVal()       # the resultant

########################################################################

if __name__ == '__main__':

    expression1 = "( ( 7 + 3 ) * ( 5 - 2 ) )"
    expression2 = "( 3 * ( 4 + 8 ) )"

    parse_tree1 = buildParseTree(expression1)
    parse_tree2 = buildParseTree(expression2)

    resultant_of_tree1 = evaluatePraseTree(parse_tree1)
    resultant_of_tree2 = evaluatePraseTree(parse_tree2)

    print(f"The result of calculating the parse tree1: {resultant_of_tree1}")
    print(f"The result of calculating the parse tree2: {resultant_of_tree2}")