class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return f"Node({self.data or 'None'}, {self.next.data or 'None'})"


class LinkedList:
    def __init__(self, nodes):
        self.head = None
        self.tail = self.head
        self.length = 0

        first_node, *nodes = nodes
        node = Node(first_node)
        self.head = node
        self.tail = node
        self.length += 1

        for data in nodes:
            self.append(data)

    def __str__(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(node.data)
            node = node.next
        return '->'.join(nodes)

    def __repr__(self):
        print('__repr__ called')
        node = self.head
        nodes = []
        while node.next is not None:
            print(node)
            nodes.append(str(node))
            node = node.next
        return '->'.join(nodes)

    def traverse_to_index(self, index):
        counter = 0
        current_node = self.head

        while counter != index:
            current_node = current_node.next
            counter += 1
        return current_node

    def append(self, data):
        node = Node(data)
        self.tail.next = node
        self.tail = node
        self.length += 1

    def prepend(self, data):
        node = Node(data)
        node.next = self.head
        self.head = node
        self.length += 1

    def insert(self, index, data):
        print(f'Inserting {data} at index {index}')
        if index >= self.length:
            self.append(data)
        else:
            leader = self.traverse_to_index(index-1)
            new_node = Node(data)
            new_node.next = leader.next
            leader.next = new_node
        self.length += 1

    def remove(self, index):
        print(f'Removing node at index {index}')
        if index <= self.length:
            leader = self.traverse_to_index(index-1)
            node_to_remove = leader.next
            leader.next = node_to_remove.next
            self.length -= 1

    def reverse(self):
        node = self.head
        nodes = LinkedList(node.data)
        while node.next:
            node = node.next
            nodes.prepend(node.data)
        return nodes


llist = LinkedList(['a', 'b', 'c', 'd'])
print(llist)
llist.prepend('z')
print(llist)
llist.append('yy')
print(llist)
print(llist.traverse_to_index(3))
llist.insert(3, 'dd')
print(llist)
llist.remove(2)
print(llist)
print(llist.reverse())
repr(llist)
