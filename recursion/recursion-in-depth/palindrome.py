# palindromes: kayak, toot, maaam, ..
# write two functions that gonna check whether a string is a plindrome of not
# recursievly and iteratively

# iteratively: we are going to use a deque data structure
def remove_first(deque):
    i = 0
    return deque.pop(i) 

def isPalindrome(string):
    
    deque = []
    for char in string:
        deque.append(char)
    
    while len(deque) != 0 and len(deque) > 1:
        if remove_first(deque) != deque.pop():
            return False
    return True



def isPailndromeRecursively(string):
    
    if (len(string) == 0 or len(string) == 1):
        return True

    if (string[0] == string[len(string)-1]):
        return isPailndromeRecursively(string[1:len(string)-1])

    return False


if __name__ == '__main__':
    print(isPailndromeRecursively('maam'))
    print(isPailndromeRecursively('mysql'))
    print(isPailndromeRecursively('rececar'))
    print(isPailndromeRecursively('ddd'))
    print()
    print(isPalindrome('kayak'))
    print(isPalindrome('nannn'))
    print(isPalindrome('hello'))
    print(isPalindrome('myym'))
