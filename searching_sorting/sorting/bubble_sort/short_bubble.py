"""
In the short bubble sort algorithm, we have to check if the array is sorted earlier
we have to break the looping to save this time of non necessary iteration

if the array is sorted is going to break out without wasting time

"""

def shortBubbleSort(arr):

    pass_num = len(arr) - 1
    is_sorted = True

    while pass_num > 0 and is_sorted:
        is_sorted = False       # to stop iterating

        for i in range(pass_num):
            if arr[i] > arr[i+1]:
                is_sorted = True
                # swap
                arr[i], arr[i+1] = arr[i+1], arr[i]

                # decrement
                pass_num -= 1

if __name__ == '__main__':
    array = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    print(f"nonSorted: {array}")
    
    # sort the array
    shortBubbleSort(array)
    print(f"Sorted: {array}")