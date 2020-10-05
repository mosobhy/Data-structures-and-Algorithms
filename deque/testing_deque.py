# in this script, iam gonna test the method of the deque data structure
from deque import Deque

def main():
    
    # create a new deque
    d = Deque()

    # add element
    print()
    print('add front')
    d.add_front(6)
    d.show()

    # add rear
    print()
    print('add rear')
    d.add_rear(5)
    d.show()

    # add front
    print()
    print('add front')
    d.add_front(10)
    d.show()

    # add rear my name
    print()
    print('add rear')
    d.add_rear('mohamed sobhy')
    d.show()

    # remove the front elemtn
    print()
    print('remove front')
    print(d.remove_front())
    d.show()

    # remove rear element
    print()
    print('remove rear')
    print(d.remove_rear())
    d.show()


if __name__ == '__main__':
    main()