'''Develop a python program to create two classes 
called as Stack and Queue. Provide the necessary data members 
and methods to display the operations that can be 
performed on stacks and queues. Test for all type of conditions.'''

class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        return "Stack is empty"

    def is_empty(self):
        return len(self.items) == 0

    def display(self):
        return self.items

class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        return "Queue is empty"

    def is_empty(self):
        return len(self.items) == 0

    def display(self):
        return self.items

# Testing the Stack class
stack = Stack()
print("Stack operations:")
stack.push(1)
stack.push(2)
stack.push(3)
print("Stack after pushes:", stack.display())
print("Popped from stack:", stack.pop())
print("Stack after pop:", stack.display())
print("Is stack empty?", stack.is_empty())

queue = Queue()
print("\nQueue operations:")
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
print("Queue after enqueues:", queue.display())
print("Dequeued from queue:", queue.dequeue())
print("Queue after dequeue:", queue.display())
print("Is queue empty?", queue.is_empty())
