'''
here you are going to iterate over the n and check if the guess is valid or not

'''

def getSqrt(n):

    guess = 1
    while guess ** 2 != n:
        guess += 1

    return guess

if __name__ == '__main__':
    num = int(input())
    print(getSqrt(num))

'''
the runtime for this algorithm is O(sqrt(n)) because the iteration condition is equievelant
to this:
    guess != sqrt(n)
'''

