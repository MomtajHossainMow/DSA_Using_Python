"""
A linked list is a linear data structure, in which the elements 
are not stored at contaguous memory location. The elements in 
a linkedlist are linked usin pointers.
"""

#Node Class
class Node:
    #Function to initialize the node object
    def __init__(self, data):
        self.data = data    #Assign data
        self.next = None    # Initialize next as null

#Linked List Class
class LinkedList:
    #Function to initialize the Linked List object
    def __init__(self):
        self.head = None
    
    #This function prints contents of linked list stating from head
    def printList(self):
        temp = self.head
        while (temp):
            print(temp.data)
            temp = temp.next
            

#Code execution starts from here
if __name__=='__main__':
    #Start with the empty list
    llist = LinkedList()

    llist.head = Node(1)
    second = Node(2)
    third = Node(3)
"""
Three nodes have been created.
We have references to these three blocks as head, second and third
    llist.head     second             third
        |             |                 |
        |             |                 |
    +----+------+     +----+------+     +----+------+
    | 1 | None |     | 2 | None |     | 3 | None |
    +----+------+     +----+------+     +----+------+
"""
# Link first node with second
llist.head.next = second
"""
Now next of first Node refers to second. So they both are linked.

    llist.head     second             third
        |             |                 |
        |             |                 |
    +----+------+     +----+------+     +----+------+
    | 1 | o-------->| 2 | null |     | 3 | null |
    +----+------+     +----+------+     +----+------+
"""
# Link second node with the third node
second.next = third
"""
Now next of second Node refers to third. So all three nodes are linked.

    llist.head     second             third
        |             |                 |
        |             |                 |
    +----+------+     +----+------+     +----+------+
    | 1 | o-------->| 2 | o-------->| 3 | null |
    +----+------+     +----+------+     +----+------+
"""

### Linked List Traversal
llist.printList()