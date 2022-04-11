'''
the idea of converting the deciaml numbers to its binary representation
is to keep dividing by 2 and keep track of the remainder
till we get to zero where we can not divide so return the whole tracked remainder
'''


def decimalToBinary(decimal, result=''):
    
    # the base case is zero where we have to stop dividing and return resutl
    if (decimal == 0):
       return result
  
  # keep track of the remainders 
    result = str(decimal % 2) + result
    return decimalToBinary(decimal // 2, result)

if __name__ == '__main__':
    
    print(decimalToBinary(123))
