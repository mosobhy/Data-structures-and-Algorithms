'''
The selection sort is an improvement upon the bubble sort...
since here we will make just a single swap for each pass
and in order to do this, we will have to keep track of the largest item 
in each pass and place it in its proper place and this technique will reduce the number
of swaps we do which leads to be faster than bubble sort

the Runtime complexity will be also as the bubble sort O(n^2)


'''
def selectionSort(arr):
    for pass_num in range(len(arr)-1, 0, -1):
        largest = 0     # will be the index of the largest item in the array
        for i in range(1, pass_num+1):  # i have started from 1 in this loop becasue i will use largest to dereference the 0 in every pass
            if arr[i] > arr[largest]:
                largest = i

        # swap with the last item in this pass
        temp = arr[pass_num]
        arr[pass_num] = arr[largest]
        arr[largest] = temp


if __name__ == '__main__':
    array = [20, 30, 40, 90, 50, 60, 70, 80, 100, 110]

    print(f"nonSorted: {array}")

    selectionSort(array)

    print(f"Sorted: {array}")