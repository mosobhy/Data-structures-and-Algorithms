'''
The key concept of this file to use recursion in all of the
linked list operations
'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    
    def __str__(self):
        return f"Node: {self.data}"

class LinkedList:
    id = 0

    # class method to increment the class attr id
    @classmethod
    def _incrementId(cls):
        cls.id += 1
        return cls.id

    def __init__(self):
        print(f'LinkedList Initialized: {LinkedList._incrementId()}')
        self.size = 0
        self.head = None    # of type Node

    def insertNode(self, node): # start will be passed as linkedlist.head
        ''' Voidly inserts a node at the end of the linked list '''
        nodePtr = self.head 
        if nodePtr == None:
            self.head = node
        else:
            while nodePtr.next != None:
                nodePtr = nodePtr.next
        
            nodePtr.next = node
        print('done node: ', node.data)

    def insertNodeAtPos(self, node, pos):
        ''' Voidly insert a node a specific position '''
        currentPtr = self.head
        prevPtr = self.head
        counter = 0

        while currentPtr.next != None and counter <= pos:
            prevPtr = currentPtr
            currentPtr = currentPtr.next
            counter += 1
        
        node.next = currentPtr
        prevPtr.next = node


    def findNode(self, val):
        ''' Returns True if a Node exits in the linked list False otherwidse '''
        nodePtr = self.head

        while nodePtr.next != None:
            if nodePtr.data == val:
                return True
            else:
                nodePtr = nodePtr.next

        return False

    def deleteNode(self, val):
        ''' Voidly deletes a node(data) from the linked list '''
        currentPtr = self.head
        prevPtr = self.head
        while currentPtr.next != None:
            if currentPtr.data == val:
                # isolate the current node to be deleted by the garbage collector
                prevPtr.next = currentPtr.next
                break

            else:
                prevPtr = currentPtr
                currentPtr = currentPtr.next

# this algorithms is very important
    def reverseList(self, node):
        ''' Recursive function that reverse the linked list ''' 
        if node == None or node.next == None:
            return node
        head = self.reverseList(node.next)
        node.next.next = node
        node.next = None

        return head 

    def ListTraversal(self, head):
        ''' Print all node of the linked list '''
        if head != None:
            print(head.data, end='->')
            self.ListTraversal(head.next)