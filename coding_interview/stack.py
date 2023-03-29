class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        _next = self.next.value if self.next else 'None'
        return f"Node({self.value}, {_next})"


class Stack:
    def __init__(self):
        self.top = None
        self.bottom = None
        self.length = 0

    def __str__(self):
        node = self.top
        nodes = []
        while node is not None:
            nodes.append(str(node))
            node = node.next
        return '->'.join(nodes)

    def peek(self):
        return self.top

    def push(self, value):
        new_top = Node(value)
        new_top.next = self.top
        self.top = new_top
        self.length += 1

    def pop(self):
        top = self.top
        self.top = top.next
        self.length -= 1
        return top

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
