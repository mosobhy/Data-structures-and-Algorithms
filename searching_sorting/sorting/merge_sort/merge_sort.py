'''
Merge sort a divide and conquer algorthim which means that its divid the unsorted array
into two halves and recursively do this operation till dividing the whole array into arrayes of single
item (and array of size of 1 is a sorted array by definition)

after that now merging the whole sorted arrayes into the original array by iterating over each
half and apply checks for each iteration, put the smaller into the original array..

the run time complextiy for this algorithm is comprised of two parts..
1. the dividing part, in which we divid the array into halves each time, so O(log n) where n is the length of the array
2. the merging part, in which we merge the small sorted arrays into the orginal array, so O(n) where n is the lenght of teh array

so the overall time complexity is O(n log n)
'''

def mergeSort(arr):
    print('dividing array ', arr)

    # set the base case, which is going to represent the single sorted array(of size one)
    if len(arr) > 1:
        mid = len(arr) // 2

        # get the left half and right half
        left_half = arr[:mid]
        right_half = arr[mid:]

        # recursively call the mergeSort function upon each half to divid them till
        # it get to an array of size one, and then it will apply the merging part
        mergeSort(left_half)
        mergeSort(right_half)

        # now lets merge the sorted smallest arrays
        i = 0   # a pointer to keep track of our advance in the left half
        j = 0   # a pointer to keep track of our advance in the right half
        k = 0   # a pointer to keep track of our last insert into the original array (arr)

        # iterate over the two halves and apply check
        while i < len(left_half) and j < len(right_half):
            # check for the smaller item and insert it into the original array
            if left_half[i] < right_half[j]:
                # insert the current indexed left half value in the original list
                arr[k] = left_half[i]
                # advance the pointer of left and original
                i += 1
                k += 1
            else:
                # insert the current indexed right half value in the original list
                arr[k] = right_half[j]
                j += 1
                k += 1

        # the purpose of this to iterate over the left and right halves again and check if
        #  any values are left in teh array and bring them in the current pointed at index
        #  in the original array

        # now i need to iterate over the left values in the left and right halves and insert them into the original array, as are performing the above mergin we will have some items are left into the each half, so i need to get them into the original aray into the right position
        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

        print("Merging array: ", arr)


if __name__ == "__main__":
    array = [54, 26, 93, 17, 77, 31, 44, 55, 20]

    print(f'Before sorting the array: {array}')

    mergeSort(array)

    print(f'After sorting the array: {array}')


"""
There is still some margin of optimization for this implmentation, since the slice oprator
consumes O(k) time (k is the slice size), so all to do is to pass the starting and ending indecies
along with list when we make the recursive call


Although this algorithm is faster that the insertion sort in terms of time, but its wrose than 
insertion sort in terms of memory usage, since this algorthims uses two arrays to store the
original array's halves and this could be memory problematic when it comes to large datasets arrays
"""