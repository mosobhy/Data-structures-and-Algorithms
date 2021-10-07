from LinkedList import Node, LinkedList


ll = LinkedList()

head = Node(0)
ll.insertNode(head)

for i in range(1, 5):
    ll.insertNode(Node(i))

ll.ListTraversal(head)

ll2 = LinkedList()

head2 = Node(0)
ll2.insertNode(head2)
for i in range(1, 100):
    ll2.insertNode(Node(i))

ll2.ListTraversal(head2)