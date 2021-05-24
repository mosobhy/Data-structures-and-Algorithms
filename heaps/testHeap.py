'''
In this file i am going to test the heap implemetation

'''

from MinHeap import MinHeap



def main():

    my_heap = MinHeap()

    my_heap.insert(5)
    my_heap.insert(7)
    my_heap.insert(3)
    my_heap.insert(11)
    my_heap.insert(9)
    my_heap.insert(18)
    my_heap.insert(14)

    print('Min heap1..............')
    my_heap.display()

    print('############################')


    # lets build a min heap out of alist of items
    print("Min heap2 which we have composed of the list [9,6,5,2,3]")

    items = [9, 6, 5, 2, 3]
    my_heap2 = MinHeap()
    my_heap2.buildHeap(items)

    my_heap2.display()

    print('getting the least element of the heap')
    for i in range(my_heap2.size()):
        print(f'min {i} is: {my_heap2.delMin()}')

    print()
    print('at the end of the extraction we have nothing into the heap')
    my_heap2.display()


if __name__ == '__main__':
    main()