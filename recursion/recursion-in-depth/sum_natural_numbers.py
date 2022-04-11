
def sumNatural(num):
    summation = 0
    for i in range(num+1):
        summation += i
    return summation 

def sumNaturalRecursively(num, result=0):
    if (num == 0):
        return result
    result = result + num
    return sumNaturalRecursively(num-1, result)

def sumNaturalRecursively2(num):
   if num <= 1:
       return num 
   return num + sumNaturalRecursively2(num - 1)


if __name__ == '__main__':

    print(sumNatural(10))
    print(sumNaturalRecursively(10))
    print(sumNaturalRecursively2(10))
