'''
This algorithm divides the sorted array into two halves.. picking up the middle element and check
for the target element.. if its greater.. so pick the middle of the right side and check for it 
and so on till find the element

you could think of the way to solve it, as you have two pointers low and high
low is pointing at the first index of arr
high is pointing at the last index of arr

{{ ITERATIVE }}
if the arr[mid] < target:       we are searching for element 7
    go right by moving the 
    low pointer to point at the 
    index after mid
    low = mid + 1
elif the arr[mid] > target:
    go left by moving the 
    high pointer to point at the 
    index before mid
    high = mid - 1
else:: arr[mid] == target:
    return target or True or whatever you would return


At the very begining... 

low = 0
high = len(arr) - 1
mid = -1

        0                               7
        ---------------------------------
        | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
        ---------------------------------
          ^                           ^
          |                           |
         low                         high


Pick the mid element of the arry
mid = (low + high) // 2
      (  0 +   7  ) // 2 ==> 3


        0             3                7
        ---------------------------------
        | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
        ---------------------------------
          ^           ^               ^
          |           |               |
         low         mid             high


Check if the arr[mid] < target:
so we have to move to right via updating the low pointer to be at
the index after the current mid
        low = mid + 1
            = 3 + 1 ===> 4


        0             3                7
        ---------------------------------
        | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
        ---------------------------------
                      ^    ^           ^
                      |    |           |
                     mid  low         high


Now the mid is going to be updated via
to get the middle index between the new
high and low pointers
mid = (low + high) // 2
      (  4 +  7  ) // 2 ===> 5


        0                 4   5        7
        ---------------------------------
        | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
        ---------------------------------
                          ^   ^        ^
                          |   |        |
                         low  mid     high


Again, we have to check 
if arr[mid] < target:
    got right by moving the low
    pointer to point at the index after mid

and update the mid 


        0                     5        7
        ---------------------------------
        | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
        ---------------------------------
                              ^   ^    ^
                              |   |    |
                             mid low  high


so picking up the middle of the new
array between low and high
mid = (low + high) // 2
    = (6 + 7 ) // 2 ===> 6


        0                         6    7
        ---------------------------------
        | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
        ---------------------------------
                                  ^    ^
                                  |    |
                                 low  high
                                 mid


now check if the arr[mid] < target:
            and this case: yes we search for 7
            so return True


'''




def recursive_binary(List, target):
    List = sorted(List)
    
    if len(List) == 0:
        return False
    else:
        mid = (len(List) - 1) // 2

        if List[mid] < target:
            # go in right direction with a shorted list
            return recursive_binary(List[mid+1:], target)
        elif List[mid] > target:
            # go in left direction with a shorted list
            return recursive_binary(List[:mid], target)
        else:
            return mid






def iterative_binary(List, target):
    # we pick the middle index not element to avoid if the elements are repeated.
    List = sorted(List)

    # assign the two pointers one at first element, high at the last element
    low = 0
    high = len(List) - 1
    
    while low <= high:
        # pick up the middle of the array
        mid = (low + high) // 2

        # check upon the middle element
        if List[mid] < target:
            # go right via moving the low pointer to the index after the mid
            low = mid + 1
        elif List[mid] > target:
            # go left via updating the high pointer to the index before mid
            high = mid - 1
        else:
            # this equlity.. so return the index of the target
            return mid
    
    return 'NOT FOUND'   # Error







if __name__ == '__main__':
    arr = list(map(int, input().split()))
    item = int(input())

    print(f'Recursive approach: {recursive_binary(arr, item)}')
    print(f'Iterative approach: {iterative_binary(arr, item)}')