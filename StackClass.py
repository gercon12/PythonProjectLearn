
s = []
s.append("https://www.cnn.com")
s.append("https://www.cnn.com/world")
s.append("https://www.cnn.com/india")
s.append("https://www.cnn.com/china")

print(s)
print(s.pop())
print(s)

from  collections import deque
stack = deque()

print(dir(stack))

stack.append("https://www.cnn.com")
stack.append("https://www.cnn.com/world")
stack.append("https://www.cnn.com/india")
stack.append("https://www.cnn.com/china")
print(stack)
print (type(stack))

class Stack:
    def __init__(self):
        self.container  = deque()
    def push(self, val):
        self.container.append(val)
    def pop(self):
        return self.container.pop()
    def peek(self):
        return self.container[-1]
    def is_empty(self):
        return len(self.container) == 0
    def size(self):
        return len(self.container)


s = Stack()
s.push(5)
print(s.peek())
print(s.size())