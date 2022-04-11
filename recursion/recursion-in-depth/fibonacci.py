# fibonacci is a mathematical sequence where 1 , 1, 2, 3, 5, 8, 13, 21, ...
def fibonacci(num):
    if num == 0 or num == 1:
        return 1
    
    #     this executes first    then this
    #          |                    |
    #          v                    v  
    return fibonacci(num - 1) + fibonacci(num - 2)

if __name__ == '__main__':
    print(fibonacci(3))


'''
note about binary recursive calls
1. the left recursive call will have to be evaluated first before touch the right one
'''
