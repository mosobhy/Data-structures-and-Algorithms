from functools import lru_cache
import time

# Adding lru_cache annotation ensures that if the function has been called recently for a particular value, it will not recompute that value, but use a cached previous result
@lru_cache(maxsize=None)
def fibWithLRU(n):
    if n == 0 or n == 1:
        return 1
    
    return fibWithLRU(n - 1) + fibWithLRU(n - 2)


def fibWithoutMemo(n):
    if n == 0 or n == 1:
        return 1
    return fibWithoutMemo(n - 1) + fibWithoutMemo(n - 2)


if __name__ == '__main__':

    n = 30

    time1_s = time.time()
    output1 = fibWithoutMemo(n)
    time1 = (time.time() - time1_s) * 1000

    time2_s = time.time()
    output2 = fibWithLRU(n)
    time2 = (time.time() - time2_s) * 1000

    print(f'output without memo: {output1} and took: {time1}')
    print(f'output with memor: {output2} and took: {time2}')