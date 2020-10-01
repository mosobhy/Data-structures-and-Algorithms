from stack import Stack

# instantiate a stack object
st = Stack()

# show the stack
st.showStack()

# push some elements to the stack
st.push(1)
st.push(2)
st.push(3)
st.push(4)
st.push(5)

st.showStack()

# use the size method
print(f'the lenght of the stack is: {st.size()}')

# the peek of the stack
print(f'the peek of the stack is: {st.peek()}')

# pop the last tow elements out of the stack and put them in a tuple
print()
print('poping elements out of the stack,')
(x, y) = (st.pop(), st.pop())
print(f'x={x} y={y}')
st.showStack()
