

'''
Priority queue acts like queue in that you dequeue an item by removing it from the front
however, in a priority queue the logical order of items inside a queue is determined by
their priority. The highest priortiy items are at the front and the lowest are at the rear


So we could probably think of a couple of easy ways to implement the priority queue
1- using the sorting functions and lists... but inserting an element into a list costs
    O(n) and the sorting algorithm costs O(n log n) so the total O(n^2 log n)

2- using the binary heap, its gonna allow us both enqueue and dequeue items with the cost
    of just O(log n)   and this of course is cheaper than the way 1


so we can use a max heap or a min heap as a priority queue
'''

