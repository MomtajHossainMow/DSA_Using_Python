class Node:
    def __init__(self, data):
        #Store the value
        self.data = data
        #Point to the previous node
        self.prev = None
        #Point to the next node
        self.next = None

#Function to traverse the list in forward direction
def forward_traversal(head):
    #Initialize a pointer to the head
    curr = head
    # Traverse until the node is null
    while curr is not None:
        #Print the current data
        print(curr.data, end=" ")
        #Move to the next data
        curr = curr.next
    print()#Print a newline at the end

#Function to traverse the list in backward direction
def backward_traversal(tail):
    #Initialize a pointer to the tail
    curr = tail
    # Traverse until the node is null
    while curr is not None:
        #Print the current data
        print(curr.data, end=" ")
        #Move to the previous data
        curr = curr.prev
    print()#Print a newline at the end

if __name__ == "__main__":
    #Initialize
    head = Node(1)
    second = Node(2)
    third = Node(3)
    fourth = Node(4)

    #Link the nodes
    head.next = second
    second.prev = head
    second.next = third
    third.prev = second
    third.next = fourth
    fourth.prev = third

    #Call the traversal functions
    print("Forward Traversal: ")
    forward_traversal(head)
    print("Backward Traversal:")
    backward_traversal(fourth)