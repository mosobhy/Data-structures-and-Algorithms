'''
in here, we are going to implement a program to get the sum of a list of numbers using two 
approaches
. iterative approach (naive approach)
. recursive approach

'''

def sum_iterative(num_list):
    sum_ = 0
    for num in num_list:
        sum_ += num
    return sum_


def sum_recursive(num_list):
    """ we could think of solving this by the addition of two nums in list """
    # handle the corner cases
    if not len(num_list):
        return 0
    if len(num_list) == 1:
        return num_list[0]

    else:
        return num_list[0] + sum_recursive(num_list[1:])


if __name__ == '__main__':
    import sys
    # call the two functions
    print((sum_iterative([num for num in range(100)])))
    print((sum_recursive([num for num in range(100)])))