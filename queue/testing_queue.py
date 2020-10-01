from queue import Queue


def main():
    
    # instantiating a queue object
    queue = Queue()

    queue.enqueue('mohamed')
    queue.showQueue()
    print()

    queue.enqueue('ahmed')
    queue.showQueue()
    print()

    queue.enqueue('ali')
    queue.showQueue()
    print()

    queue.enqueue('rami')
    queue.showQueue()
    print()


    # dequeuing the queue
    print('first dequeue')
    queue.dequeue()
    queue.showQueue()
    print()

    print('seconde dequeue')
    queue.dequeue()
    queue.showQueue()
    print()

    print('third dequeue')
    queue.dequeue()
    queue.showQueue()
    print()

    print('forth dequeue')
    queue.dequeue()
    queue.showQueue()


if __name__ == '__main__':
    main()
    