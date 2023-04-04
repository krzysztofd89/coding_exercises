class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        _next = self.next.value if self.next else 'None'
        return f"Node({self.value}, {_next})"


class Queue:
    def __init__(self):
        self.first = None
        self.last = None
        self.length = 0

    def __str__(self):
        node = self.first
        nodes = []
        while node is not None:
            nodes.append(str(node))
            node = node.next
        return '->'.join(nodes)

    def peek(self):
        return self.first

    def enqueue(self, value):
        new_node = Node(value)

        if self.length == 0:
            self.first = new_node
            self.last = new_node
        else:
            self.last.next = new_node
            self.last = new_node
        self.length += 1

    def dequeue(self):
        top = self.first
        self.first = top.next
        self.length -= 1
        return top

    def is_empty(self):
        return self.length == 0


print('create queue')
new_stack = Queue()

print('add 2')
new_stack.enqueue(2)
print(new_stack.peek())
print(new_stack.length)
print(new_stack)

print('add 5')
new_stack.enqueue(5)
print(new_stack.peek())
print(new_stack.length)
print(new_stack)

print('pop')
new_stack.dequeue()
print(new_stack.peek())
print(new_stack.length)
print(new_stack)

print('pop')
new_stack.dequeue()
print(new_stack.peek())
print(new_stack.length)
print(new_stack)
