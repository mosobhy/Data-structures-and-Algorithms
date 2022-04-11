
def reverseString(string):
    wordStack = []
    for char in string:
        wordStack.append(char)
    
    reversed_word = ''
    while len(wordStack) > 0:
        reversed_word += wordStack.pop()

    return reversed_word

###################################################3
def recursivelyReverseString(string):

    # base case which we have to move forward
    if (string == ''):
        return ''

    # recursively shrink the string
    return recursivelyReverseString(string[1:]) + string[0]

if __name__ == '__main__':
    print(reverseString('hello'))
    print(recursivelyReverseString('hello'))
