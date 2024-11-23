class Stack:
    def __init__(self):
        self.stack = []  # Initialize the stack as an empty list

    # Push an element onto the stack
    def push(self, item):
        self.stack.append(item)
    
    # Pop an element from the stack and return it
    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        else:
            return "Stack is empty"
    
    # Peek at the top element of the stack
    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        else:
            return "Stack is empty"
    
    # Check if the stack is empty
    def is_empty(self):
        return len(self.stack) == 0


# Testing the Stack implementation

stack = Stack()

# Push elements onto the stack
stack.push(10)
stack.push(20)
stack.push(30)

# Pop an element and display the result
popped_element = stack.pop()
print(f"Popped element: {popped_element}")

# Peek at the top element of the stack
top_element = stack.peek()
print(f"Top element after pop: {top_element}")

