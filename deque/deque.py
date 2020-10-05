'''
The deque: is linear data structure which provides all the capabilities of both stack and queue DS
which means that you can add elements inside this deque from both sides and also remove elements
from both sides
NOTE: you have to keep track of the [rear] element and the [head] element



                        rear(tail)              front(head)
                        -------  ------  ------  ------
                        | data || data || data || data |  
                        -------  ------  ------  ------

Deque operations
----------------
Deque()   >>> instantiates a new deque and returns nothing
isEmpty() >>> checks if the deque is empty or not via its lenght
add_front(element)  >>> inserts an element to the last index of the list using append()
add_rear(element)   >>> inserts an element to the position zero  insert(0, element)
remove_front()      >>> return the last element in the list and remove it   pop()
remove_rear()       >>> return the first element in the list and remove it 
size()              >>> return the length of the list

'''

class Deque:
    # what to be initialized within the constructor
    def __init__(self):
        self.elements = []

    def isEmpty(self):
        if len(self.elements):
            return False # not empty
        return True # empty

    def add_front(self, element):       # equevilant to the push() in stack
        self.elements.append(element)
    
    def add_rear(self, element):        # equevilant to the enqueue() in queue
        self.elements.insert(0, element)

    def remove_front(self):             # equevilant to the pop() and dequeue()
        return self.elements.pop()

    def remove_rear(self):
        return self.elements.pop(0)

    def size(self):
        return len(self.elements)

    def show(self):
        for element in self.elements:
            print(f'{element} || ', end='')
        print()

    

