# we can refere to the linked list with an unordered list as an ADT(abstract data type)

# this is the typical node implementation.
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    # make the setter functions.
    def set_data(self, data):
        self.data  = data
    
    def set_next(self, next):
        self.next = next

    # make the getter functions
    def get_data(self):
        return self.data

    def get_next(self):
        return self.next

# this is the typical Linkedlist implementation.
class LinkedList:
    # what we want to initialize when instantiating new linkedlist object is making the head pointer
    def __init__(self):
        # initalize the head pointer with None to maintain the first node
        self.head = None

    def is_empty(self):
        ''' returns True if there is some nodes in the list '''
        if self.head == None:
            return True
        return False

    def insert_beginning(self, data):
        # allocate new node
        temp = Node(data)

        # first, we have to set the temp to point at the same location as the head to avoid lose access on the rest of teh list
        temp.set_next(self.head)

        # finally, assign the head to point on the temp which means make it the start of the list
        self.head = temp

    def insert_position(self, pos, data):
        # first allocate the node thats gonna be inserted in pos
        temp = Node(data)

        # make the traversing pointers
        trav = self.head
        prev = None

        if self.head == None:
            # assign the head to point at the new node
            self.head = temp

        else:
            index = 0
            while index < pos:
                prev = trav
                trav = trav.get_next()
                index += 1
            
            temp.set_next(trav)
            prev.set_next(temp)

    def append(self, data):
        pass

    def size(self):
        pass

    def search(self, data):
        pass

    def remove(self, data):
        pass

    def show_list(self):
        pass
    


