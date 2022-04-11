'''
memoization is a technique of optimizing binary recursion
Memoization effectively refers to remembering ("memoization" → "memorandum" → to be remembered)
results of method calls based on the method inputs and then returning the remembered result rather
than computing the result again. You can think of it as a cache for method results. 
'''
import time

# implementing fibonacci without memoization
def fibWithoutMemo(n):
    if n == 0 or n == 1:
        return 1
    return fibWithoutMemo(n-1) + fibWithoutMemo(n-2)


# implementing memoization using dictionaries
def fibHelper(n):
    ''' here is the helper function of the recursive function'''
    memo = {}
    return fibWithMemo(n, memo)

def fibWithMemo(n, memo):
    ''' here is the recursive function that calcuates the fibonacci'''
    if n == 1 or n == 0:
        return 1
    if n not in memo:
        memo[n] = fibWithMemo(n-1, memo) + fibWithMemo(n-2, memo)
    return memo[n]


if __name__ == '__main__':

    n = 30

    print('Without Memo......')
    time_start = time.time()
    output1 = fibWithoutMemo(n)
    time1 = (time.time() - time_start) * 1000 
    print(f'ouput without memoization: {output1}\nand took: {time1}')

    print('With Memo.....')
    time2_start = time.time()
    output2 = fibHelper(n)
    time2 = (time.time() - time2_start) * 1000
    print(f'output with memoization: {output2}\nand took: {time2}')
