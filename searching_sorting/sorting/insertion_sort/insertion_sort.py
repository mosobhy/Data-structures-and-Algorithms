'''
actully this algorithm pefroms faster than the selecitno and bubble sort since it works as
. it maintains a sorted sublist starting at postion 1 in teh array and at each pass
it simply checks the current value agasint every item in the behind sorted sublist, and shift 
the greater items to right till hitting a smaller item or hitting the begining of the list
and then insert the current value into it.. and this gurantees that we have a sorted sublist behind
so we can add a new item to it at each iteration till having the whole array.

this alogrithms performs n - 1 passes upon the array

and the overall runtime O(N ^ 2)

'''

def insertionSort(arr):

    # iterate over the array starting from index 1 and thats mean that the index of 0 is composing an already sorted array of size one element
    for index in range(1, len(arr)):
        # keep track of the current value.. since we may encounter multiple shifts so this will overwrite and we still need it to insert it in its proper position
        current_value = arr[index]

        # make a copy of the iteration index since we will use it to iterate backwardly.. and we don't need to decrement the iterator of the for loop
        current_pos = index

        # iterate backwardly and check for larger items, shuffle them while iterating..
        while current_pos > 0 and current_value < arr[current_pos - 1]:
            # shuffle
            arr[current_pos] = arr[current_pos - 1]

            # decrement the current pos to move back for one item
            current_pos -= 1

        # now we break out of the loop because of reaching the begining of arr of find the a smaller item
        # so insert the current item in this position
        arr[current_pos] = current_value

if __name__ == '__main__':
    
    # array to sort
    array = [54, 26, 93, 17, 77, 31, 44, 55, 20]

    print(f"Before sorting: {array}")

    insertionSort(array)

    print(f"After Sorting: {array}")
