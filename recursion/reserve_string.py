'''
there are some ways to reserve strings in pytohn,, but here i am gonna reverse it
using two approaches 
1. iterative
2. recursive
3. stack 

'''
def stack_reverse(string):
    # push all chars into the stack
    stack = []
    for char in string:
        stack.append(char)
    
    reversed_string = ''
    for _ in range(len(stack)):
        reversed_string += stack.pop()

    return reversed_string


def iterative_reverse(string):
    
    reversed_string = ''
    for char in string:
        reversed_string = char + reversed_string

    return reversed_string

def recursive_reverse(string):
    # base case
    if len(string) == 0:
        return string
    else:
        return recursive_reverse(string[1:]) + string[0]

def built_in_reverse(string):
    return string[::-1]

def built_in_reverse2(string):
    reversed_string = ''
    return reversed_string.join(reversed(string))


if __name__ == '__main__':
    # call this fucking method
    print(stack_reverse('hello world'))
    print(iterative_reverse('hello world'))
    print(recursive_reverse('hello world'))
    print(built_in_reverse('hello world'))
    print(built_in_reverse2('hello world'))



