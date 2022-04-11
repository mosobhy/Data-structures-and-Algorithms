# merge Sort Alogrithm using divid and conquer strategy
def mergeSort(array):
    
    if len(array) > 1:
        mid = len(array) // 2
        
        leftSubArr = array[:mid]
        rightSubArr = array[mid:]

        # recursion
        mergeSort(leftSubArr)
        mergeSort(rightSubArr)

        # merging in order
        i = 0   # left pointer
        j = 0   # right pointer
        k = 0   # index array pointer
        while i < len(leftSubArr) and j < len(rightSubArr):
            if leftSubArr[i] < rightSubArr[j]:
                array[k] = leftSubArr[i]
                i += 1 
                k += 1
            else:
                array[k] = rightSubArr[j]
                j += 1
                k += 1


        while i < len(leftSubArr):
            array[k] = leftSubArr[i]
            i += 1
            k += 1

        while j < len(rightSubArr):
            array[k] = rightSubArr[j]
            j += 1
            k += 1

if __name__ == '__main__':
    array = [99, 80, 400, 2, -1, 0, 11]
    print('before sorting: ', array)
    mergeSort(array)
    print('after sorting: ', array)
