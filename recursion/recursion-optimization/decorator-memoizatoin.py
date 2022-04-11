

# build the memoization class
class Memoize:
    def __init__(self, func):
        self.func = func
        self.memo = {}

    def __call__(self, *args):
        if args in self.memo:
            self.memo[args] = self.func(*args)
        return self.memo[args]


@Memoize
def fibWithDecoratorMemo(n):

    if n == 1 or n == 0:
        return 1
    
    return fibWithDecoratorMemo(n-1) + fibWithDecoratorMemo(n-2)



if __name__ == "__main__":

    n = 10

    result = fibWithDecoratorMemo(n)
    print(f'fibannaci of 10: {result}')
