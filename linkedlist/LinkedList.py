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
        # we need to allocate the new node
        temp = Node(data)

        # check if the linked list is not empty do traverse teh linked list
        if self.head:
            # we need to iterate over the lined list using a pointer taking the first head node value
            trav = self.head

            # iterate over the whole linked list to the reach the last node
            while trav.get_next():
                trav = trav.get_next()

            trav.set_next(temp)
        
        else:
            # the linked list is empty, assign directly
            self.head = temp

    def size(self):
        '''this method is gonna return the length of the linked list as an integer value '''
        # assign the trav pointer to point at the same node as the head
        trav = self.head

        # check if the head not None, so now iterate and count
        if self.head:

            # set the counter to 0
            counter = 0

            # iterate over the list
            while trav.get_next() and trav.get_data():
                counter += 1
                
                # move the trav
                trav = trav.get_next()
            
            return counter
        else:
            return 0

    def search(self, data):
        ''' 
            this method is gonna take a value representes the data we need to search for and
            returns the index of this value in the list
        '''
        if self.head:

            # make the traveser pointer and assign it to head
            trav = self.head
            counter = 0

            # iterate over the list and apply the check
            while trav.get_next():
                counter += 1

                # check the data
                if trav.get_data() == data:
                    # returning a boolean of true and the index of this item in the list
                    return [True, counter]

                else:
                    # advance the trav pointer
                    trav = trav.get_next()
            
            # not found 
            return False

        # no list
        else:
            return False

    def remove(self, data):
        '''
            this method remove a particular node from the list 
            this method assume that there are nodes in the list
        '''
        if self.head:
            trav = self.head
            prev = trav

            # check for the first node
            if trav.get_data() == data:
                self.head = trav.get_next()
            else:
                
                # iterate over the linked list and check with data contained inside each node
                while trav.get_data() is not data:
                    prev = trav
                    trav = trav.get_next()
                
                # remove the this node that the trav pointing at.
                prev.set_next(trav.get_next())
        else:
            raise 'No List Yet'


    def removeList(self):
        ''' this method should remove the whole linked list and return true after '''
        # its easy to remove the whole linked list in python than in C, it just set the head to point at None and the python garbage collection process will do the rest
        self.head = None

    def sort(self, sorting_algorithm):
        ''' 
            this method should sort the list of which contains integer values
            INPLACE(which means not to make a new datastructre to store the output)
            The default algorithm that i gonna use in this function to sort the list is standard sort algorithm
        '''
        pass

    def pop(self):
        ''' this method should return the last node in the list and also remove it from the list '''
        pass

    def showList(self):
        ''' this method should dispaly the linked list '''
        if self.head:
            trav = self.head

            while trav.get_next():
                print(str(trav.get_data()), end=' >> ')
                
                # advance the trav to the next node
                trav = trav.get_next()

            # print the last node data manually
            print(str(trav.get_data()))
            print()
        else:
            raise 'No List Yet!'
    


def main():
  lo = LinkedList()

  for num in range(500):
    lo.append(num)

  lo.showList()

  print(f'the lenght of the list is {lo.size()}')


if __name__ == '__main__':
  main()