# binary search is a great example of divide and conquer algorithms 
# it takes a sorted array and searchs for a target element 

def binarySearch(arr, left, right, target):
    
    if len(arr) == 0:
        return False

    else:
        mid = (left + right) // 2

        if arr[mid] == target:
            return mid

        if arr[mid] < target:
            # move the left pointer to the mid pos
            left = mid+1
            return binarySearch(arr, left, right, target)

        # move the right to the mid pos
        return binarySearch(arr, left, mid, target)


def binarySearchRec(arr, target):
    left = 0
    right = len(arr) - 1
    
    return binarySearch(arr, left, right, target)


if __name__ == '__main__':
    print(binarySearchRec([-11, -6, 0, 22, 55, 88, 234543], 55))
    print(binarySearchRec([1, 2, 3, 4, 5, 6, 7], 7))
    print(binarySearchRec([1, 2, 3, 4, 5, 5, 6, 7], 1))
    print(binarySearchRec([1, 2, 3, 4, 5, 5, 6, 7], 3))

