"""
to check if a string is a plindrome or not using recursion,, there is a very easy trick
to takcle this problem... 

THE APPROACH is:
. we have to reverse the string using a recursive algorithm
. check if the revered string == the original string
    . this is a plindrome string (True)

"""

# make the recursive function that reveres a string
def reverse_string(string):

    if len(string) == 0 or len(string) == 1:
        return string

    else:
        return reverse_string(string[1:]) + string[0]       # concatination


# make the function that checks
def isPalindrome(string):
    # reverse the string
    string_ = reverse_string(string)

    # check if a reversed string and the original one are equals.. return true
    if string == string_:
        return True
    return False


if __name__ == '__main__':

    str_to_check = input('Enter a str: ')

    print(isPalindrome(str_to_check))

