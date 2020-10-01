'''
The stack DS is very useful when the order of the elements really matters.
You can implement the Reverse order property in the stack
You could think of any web browser back button as a stack.
'''
class Stack:
    def __init__(self):
        self.elements = []

    def push(self, data):
        self.elements.append(data)

    def pop(self):
        return self.elements.pop()
    
    def isEmpty(self):
        if len(self.elements):
            return False
        return True

    def peek(self):
        return self.elements[-1]

    def size(self):
        return len(self.elements)

    def showStack(self):
        for i in self.elements:
            print(str(i), end=' >> ')
        print()