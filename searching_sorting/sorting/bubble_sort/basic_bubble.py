'''
The bubble sort algorithms is considered the most ineffiecnet sorting algorithm since it has to 
exchange items before teh final location is known

The order of this algorithm is O((n(n-1))/2) = O(n^2)

the enhancement of this algorithm is short bubble sort and then selection sort

if you wanted to sort desendantly you will have to change the > to <

'''

def bubbleSort(arr):
    # each pass upon the list will lead to the largest item to be in its proper place
    for pass_num in range(len(arr)-1, 0, -1):
        # iterate over the array of lenght pass_num
        for i in range(pass_num):
            # check
            if arr[i] > arr[i+1]:
                # swap
                arr[i], arr[i+1] = arr[i+1], arr[i]

if __name__ == '__main__':
    array = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    print(f"nonSorted: {array}")
    
    # sort the array
    bubbleSort(array)
    print(f"Sorted: {array}")