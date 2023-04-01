class Stack:
    def __init__(self):
        self._nodes = []

    def __str__(self):
        return '->'.join([str(x) for x in self._nodes])

    @property
    def length(self):
        return len(self._nodes)

    def peek(self):
        if self.length > 0:
            return self._nodes[-1]
        else:
            return None

    def push(self, value):
        self._nodes.append(value)

    def pop(self):
        return self._nodes.pop()

    def is_empty(self):
        return self.length == 0


print('create stack')
new_stack = Stack()

print('add 2')
new_stack.push(2)
print(new_stack.peek())
print(new_stack.length)
print(new_stack)

print('add 5')
new_stack.push(5)
print(new_stack.peek())
print(new_stack.length)
print(new_stack)

print('add 22')
new_stack.push(22)
print(new_stack.peek())
print(new_stack.length)
print(new_stack)

print('pop')
new_stack.pop()
print(new_stack.peek())
print(new_stack.length)
print(new_stack)

print('pop')
new_stack.pop()
print(new_stack.peek())
print(new_stack.length)
print(new_stack)
