'''
A Palindrome: its a string that reads the same forward and backward, for exmaple, radar, toot, madam

in this problem, we are gonna use the deque data structure to build a function that takes an input
of string and check wheither its a palindrome or not

THE APPROACHE:

 - iterate over the string
    - inserts evey character to from the rear add_rear(char)
    now the front of the deque is holding the first char of the string and 
    the rear of the deque is holding the last char of the string
    , since we can remove from both the front and rear, we can compare them and continue only
    if they match. If we can keep matching first and last items, we will eventully either run out
    of chars or be left with deque of size 1 depending on whether the length of the original string
    was even or odd. In either case, the string must be a palindrome

'''
from deque import Deque

# build the function
def isPalindrome(string):
    # create the deque which will store the string
    char_deque = Deque()

    # store the string into the deque from the rear (use the deque as queue)
    for char in string:
        char_deque.add_rear(char)

    # now start to remove from both sides and compare, if matches; continue
    while not char_deque.isEmpty() and char_deque.size() > 1:
        # compare the removed from both sides, if not equal: its not a palindrome
        if char_deque.remove_front() != char_deque.remove_rear():
            return False
    
    return True

# test 
print(isPalindrome('toot'))     # true
print(isPalindrome('madam'))    # true
print(isPalindrome('hi'))       # false
print(isPalindrome('radar'))    # true
print(isPalindrome('manofsteel'))# false
print(isPalindrome('ffffffffffffffffffffffffffffffffffffffffffffffffff'))   # true