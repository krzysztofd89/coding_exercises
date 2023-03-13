class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self, nodes=None):
        self.head = None
        self.tail = self.head
        self.length = 0

        if nodes is not None:
            first_node, *nodes = nodes
            node = Node(first_node)
            self.head = node
            self.length += 1
            for data in nodes:
                node.next = Node(data)
                node = node.next
                self.length += 1
            self.tail = node

    def __repr__(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(node.data)
            node = node.next
        return '->'.join(nodes)

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

    def insert(self):
        pass

    def remove(self):
        pass

    def reverse(self):
        nodes = LinkedList()
        node = self.head
        nodes.prepend(node.data)
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
print(llist.reverse())
