# in this script i will implement the queue data strucutre
'''
The queue data structure is characterized by 'First In, First Out'
so, the operation of inserting elements in the queue is called Enqueue
the operation of poping an element out of the queue is called Dequeue
the first element is called: {{ head }} and we keep a reference of it to easily access it
the last element is called: {{ tail }} and we keep a reference of it too.

we implement the queue data structure using the python list or linked list


                          tail                    head
                        -------  ------  ------  ------
        enqueue ====>   | data || data || data || data |  ====> dequeue
                        -------  ------  ------  ------


    Enqueue: always insert in the position 0 in the list
    Dequeue: pop() the last element in the list

    NOTE: we insert in this list from the left side not appending in the last index

'''

class Queue:
    def __init__(self):
        self.elements = []

    # return the first element has been entered to the queue
    def head(self):
        return self.elements.pop()

    def tail(self):
        return self.elements[0]

    def isEmpty(self):
        return len(self.elements) == 0

    # insert the new element at the index zero (the QUEUE tail)
    def enqueue(self, data):
        self.elements.insert(0, data)
    
    # return the last the element in the list (the first element inserted) (QUEUE head)
    def dequeue(self):
        return self.elements.pop()

    def size(self):
        return len(self.elements)

    def showQueue(self):
        try:
            for element in self.elements:
                print(f'{element} || ', end='')
            print()
        except:
            raise 'No Elements'