
'''
in this problem you are supposed to get an interger as an input and 
return its square root... right this alogrithm using binary search approach

'''

def sqrt(n):
    # call another function
    return sqrt_helper(n, 1, n)


def sqrt_helper(n, Min, Max):
    
    if Max < Min:
        return -1   # no square root

    guess = (Min + Max) / 2
    
    if guess ** 2 < n:    # to low guess
        # make a higher guess
        return sqrt_helper(n, guess+1, Max)
    
    elif guess ** 2 > n:    # to high guess
        # make a lower guess
        return sqrt_helper(n, Min, guess-1)

    else:    # correct guess
        return int(guess)


if __name__ == '__main__':
    num = int(input())

    print(sqrt(num))

'''
the runtime for this algorithm equals O(log n) because we have to divide the n by 2 at every single 
iteration dude
'''