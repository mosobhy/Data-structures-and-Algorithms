# remember to solve this problem again using polymorphism
'''
# pesuduecode
RECALL:
starting with an empty stack, process the parenthesis strings from left to right, If a symbol is an
opening parenthesis, push it on the stack as a signal that a corresponding closing symbol needs to
appear later. If on the other hand, a symbol is a closing parenthesis, pop the stack. As long as it
is possible to pop the stack to match every closing symbol, the parenthesis remain balanced. If at any 
time there is no opening symbol on the stack to match a closing symobl, the string is not balanced
properly. At the end of the string, when all symbols have been precessed, the stack should be empty

the only diffirence is when a symbol is pushed into, when we find the closing symbol we need to 
check is it of the same type of the last recent opening symbol
'''

from stack import Stack

''' string = "{[()()]}" '''
def balance_symbols(string):
    # init the stack to store the most recent opening symbol
    symbols = Stack()
    index = 0

    # iterate over the string and check
    while index < len(string):
        if string[index] in '{[(':
            symbols.push(string[index])

        else:
            if symbols.isEmpty():
                return 'InBalanced'
            else:
                # does the string[index](closed bracket) matches the peek(the opened one)
                # string[index] = '{' so the peek() = '}'
                if match_symbol(string[index], symbols.peek()):
                    symbols.pop()
                else:
                    # the closed and the opened symobls are not matching
                    return 'InBalanced'
        index += 1
    
    if symbols.isEmpty():
        return 'Balanced'

    return 'InBalanced'


def match_symbol(closed, opened):
    # note that we have to put the symbols with the same index to use it to check whether they matches or not
    # because of that we cannot match using the equality operator due to '}' is not '{'
    opened_symobls = '[{('
    closed_symobls = ']})'
    
    return closed_symobls.index(closed) == opened_symobls.index(opened)


def main():

    print(balance_symbols('{([])}'))
    print(balance_symbols('{{{((([[[]]])))}}}'))
    print(balance_symbols('[[[[[[[[)'))
    print(balance_symbols('}}}{{{{'))
    print(balance_symbols('([{}])'))
    print(balance_symbols('[{()]'))


if __name__ == '__main__':
    main()