# Python program to demonstrate stack implementation using list
stack = []
# append() function to push element in the stack
stack.append("a")
stack.append("b")
stack.append("c")
print("Initial stack:", stack)
# pop() function to pop element from stack in LIFO order
print("Elements popped from stack: ")
print(stack.pop())
print(stack.pop())
print(stack.pop())
print("Stack after elements are popped: ", stack)
