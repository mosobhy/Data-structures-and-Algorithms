'''
this game looks like the musical chairs that we used to play when i was a kid

the child at the head is the child who holds the potato
dequeueing the head means that the child at the head has passed the potato the his next child

'''
from queue import Queue

# make a functino that takes a list of names and num to iterate till the num ends
# review the book of Problem solving with data structures and algorithms using python, p86
def simulate_potato(names, num):

    # declare a queue and enqueue the whole names in the list first
    game_queue = Queue()
    for name in names:
        game_queue.enqueue(name)

    # iterate until the length of the game_queue is 1(which means that the game is over)
    while game_queue.size() > 1:
        # iterate using the num range and dequeue and enquue
        for i in range(num):
            game_queue.enqueue(game_queue.dequeue())

        # after the count is over, dequeue the child who holds the potato (the one who at the head)
        game_queue.dequeue()

    # after that is done, you will have a queue with one child left whowhich is the winner, so return him
    return game_queue.dequeue()

    
print(simulate_potato(['mohamed', 'ahmed', 'ali', 'mona', 'ibrahim'], 7))
print(simulate_potato(['Bill', 'David', 'Susan', 'Jane', 'Kent', 'Brad'], 7))