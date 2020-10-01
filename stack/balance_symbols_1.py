# this is an application problem on the stack data stucture
'''
# pesuduecode

starting with an empty stack, process the parenthesis strings from left to right, If a symbol is an
opening parenthesis, push it on the stack as a signal that a corresponding closing symbol needs to
appear later. If on the other hand, a symbol is a closing parenthesis, pop the stack. As long as it
is possible to pop the stack to match every closing symbol, the parenthesis remain balanced. If at any 
time there is no opening symbol on the stack to match a closing symobl, the string is not balanced
properly. At the end of the string, when all symbols have been precessed, the stack should be empty

'''

from stack import Stack

def parenthesis_check(string):
    opend_per = Stack()     # this to store the opening parenthesis(themost recent one)
    index = 0

    # iterate over the string.
    while index < len(string):
        if string[index] == '(':
            opend_per.push(string[index])

        else:
            if opend_per.isEmpty():
                return 'InBalanced'
            else:
                opend_per.pop()
        index += 1

    if opend_per.isEmpty():
        return 'Balanced'
    return 'InBalanced'



print(parenthesis_check('((((()'))
print(parenthesis_check('((()))'))
print(parenthesis_check('))))((((('))