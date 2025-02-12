class Stack:
    def __init__(self):
        self.stack = []
        
    def push(self, value):
        self.stack.append(value)

    def pop(self):
        return self.stack.pop()

    def size(self):
        return len(self.stack)

    def peek(self):
        return self.stack[-1]

    def empty(self):
        return len(self.stack) == 0

a = eval(input())  

s = Stack()

for i in range(len(a)):
    while not s.empty() and s.peek() > 0 and a[i] < 0:
       
        if abs(s.peek()) > abs(a[i]):
            a[i] = 0  
        elif abs(s.peek()) == abs(a[i]):
            s.pop()  
            a[i] = 0
        else:
            s.pop()  
    if a[i] != 0:  
        s.push(a[i])

print('[' + ','.join(str(s.stack[i]) for i in range(s.size())) + ']')
