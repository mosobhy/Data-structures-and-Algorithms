'''
- Heap is really an interesting data structure cuz, when we visualize it as a binary tree
but implement it using a single list or array

- Binary Min heaps has a cool property which is that each node must be less than it
two children

- Min Heap operations
    1- insert(val)  # inserts an element into the array within its appropriate position
    2- delMin()     # return and remove the min element of the heap
    3- buildHeap(list)      # builds a heap (with considering the heap property and building it as a complete binary tree)
    4- size()
    5- isEmpty()

    helper functions
    1- perc_up(i)   # moving the item from buttom to its appropriate place
    2- perc-down(i) # moving the item from the top to its appropriate place down in the heap

WE can use this data structure to implement another data structure which is priorty queue (
    in which you can dequeue the element with the larges or smallest priority
)
READ IT IN Problem Solving With Algorithms and Data Strctures using Python

'''

class MinHeap:

    def __init__(self):
        self.heap = [0]
        self.current_size = 0       # we will use this as an index to the last element



    def insert(self, val):
        ''' Insert an item to the min heap '''
        # 1. append the element to the end of the list
        self.heap.append(val)
        
        # 2. increment the current size
        self.current_size += 1

        # 3. perc_up the last element.. perc_up(len(self.heap))
        self._perc_up(self.current_size)



    # helper function
    def _perc_up(self, index):       # min_heapifying
        ''' 
        This function must keep compare the current key with its parent till
        reaching the correct position
        from bottom to top
        '''
        # iterate till no parent exit
        while index // 2 > 0:
            # if the current is less than the parent
            if self.heap[index] < self.heap[index // 2]:
                # swap
                temp = self.heap[index]
                self.heap[index] = self.heap[index // 2]
                self.heap[index // 2] = temp
            
            # move to the parent
            index = index // 2



    # NOTE: DIDN'T CATCH IDEA OF THIS FUNCTION YET
    def buildHeap(self, arr):
        '''
        This function accepts an array and produce a minHeap out of it
        , it iterates over this array element by element, at each limit 
        it inserts it into the heaps and then perc_down
        '''
        index = len(arr) // 2
        self.heap = [0] + arr           # copy the elemnts of the list to heap list
        self.current_size = len(arr)    # set the size of the heap to the length of the list

        while index > 0:                # now restore the heap property
            self._perc_down(index)
            index -= 1



    def delMin(self):
        '''
        This method will return the root element (least) of the heap, and restore 
        the heap property again via applying two steps
        '''
        # 1. bring the last element in the heap to the replace the root
        min_element = self.heap[1]
        self.heap[1] = self.heap[self.current_size]
        self.heap.pop()
        self.current_size -= 1

        # 2. perc_down the new root to place it in the appropriate position
        # to restore the min heap property
        self._perc_down(1)
        
        return min_element


    # helper function
    def _perc_down(self, index):
        '''
        This method must keep swaping the new root with its greater children
        to move it to its approprate place
        '''
        while (index * 2) <= self.current_size:
            # pick the small children
            min_child_idx = self._getMinChild(index)

            if self.heap[index] > self.heap[min_child_idx]:
                # swap
                temp = self.heap[index]
                self.heap[index] = self.heap[min_child_idx]
                self.heap[min_child_idx] = temp
            
            # move to the child
            index *= 2

    
    # helper function
    def _getMinChild(self, index):
        '''
        This function is going to check which children is smaller
        and return its index
        '''
        if index * 2 + 1 > self.current_size:   # no right child exist
            return index * 2
        else:            
            if self.heap[index * 2] < self.heap[index * 2 + 1]:
                # left is smaller
                return index * 2
            else:
                return index * 2 + 1


    def size(self):
        return self.current_size


    def isEmpty(self):
        return True if len(self.heap) != 0 else False


    def display(self):
        for item in self.heap:
            print(item)

