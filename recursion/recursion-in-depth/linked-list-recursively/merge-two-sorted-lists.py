# Algorithm 1: Time: O(n) , Space: O(nm), where n is the space of list1 and m for list2
def mergeTwoLists1(list1, list2):
    newList = [None] * (len(list1) + len(list2))
    newPtr = 0
    firstPtr = 0
    secPtr = 0

    while firstPtr < len(list1) and secPtr < len(list2):
        if list1[firstPtr] < list2[secPtr]:
            newList[newPtr] = list1[firstPtr]
            firstPtr += 1
            newPtr += 1
        else:
            newList[newPtr] = list2[secPtr]
            secPtr += 1
            newPtr += 1
    return newList


def recursivelyMergeTwoLists(list1_head, list2_head):
    ''' NOTE: REMEMBER to watch the lecture of recursion provided by freecodecamp.org
    LINK: its in the file ../notesAboutRecursion 
    '''
    if list1_head == None:
        return list2_head
    if list2_head == None:
        return list1_head

    if list1_head.data < list2_head.data:
        list1_head.next = recursivelyMergeTwoLists(list1_head.next, list2_head)
        return list1_head

    else:
        list2_head.next = recursivelyMergeTwoLists(list1_head, list2_head.next)
        return list2_head


def main():
    print('hello world!')

    list1 = [1, 5, 13, 20]
    list2 = [0, 3, 4, 9, 15]
    print(mergeTwoLists1(list1, list2))

    # import the linked list class
    from LinkedList import LinkedList, Node

    n11 = Node(1)
    n12 = Node(5)
    n13 = Node(13)
    n14 = Node(20)

    n11.next = n12
    n12.next = n13
    n13.next = n14

    n21 = Node(0)
    n22 = Node(3)
    n23 = Node(4)
    n24 = Node(9)
    n25 = Node(15)

    n21.next = n22
    n22.next = n23
    n23.next = n24
    n24.next = n25

    lList1 = LinkedList()
    lList2 = LinkedList()

    lList1.insertNode(n11)
    lList1.insertNode(n12)
    lList1.insertNode(n13)
    lList1.insertNode(n14)

    lList2.insertNode(n21)
    lList2.insertNode(n22)
    lList2.insertNode(n23)
    lList2.insertNode(n24)
    lList2.insertNode(n25)

    lList1.ListTraversal()

if __name__ == '__main__':
    main()