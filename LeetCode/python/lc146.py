

class Node:
    def __init__(self, key=None, val=None, next=None):
        self.key = key
        self.val = val
        self.next = next

class LRUCache:

    # @param capacity, an integer
    def __init__(self, capacity):
        self.head = Node()
        self.tail = self.head
        self.cache = {}
        self.capacity = capacity

    def push_back(self, node):
        self.cache[node.key] = self.tail
        self.tail.next = node
        self.tail = node

    def pop_front(self):
        del self.cache[self.head.next.key]
        self.head.next = self.head.next.next
        self.cache[self.head.next.key] = self.head

    def kick(self, prev):
        node = prev.next
        if node == self.tail:
            return
        prev.next = node.next
        self.cache[node.next.key] = prev
        node.next = None
        self.push_back(node)

    # @return an integer
    def get(self, key):
        if key in self.cache:
            self.kick(self.cache[key])
            return self.cache[key].next.val
        return - 1

    # @param key, an integer
    # @param value, an integer
    # @return nothing
    def set(self, key, value):
        if key in self.cache:
            self.cache[key].next.val = value
            self.kick(self.cache[key])
        else:
            self.push_back(Node(key, value))
            if len(self.cache) > self.capacity:
                self.pop_front()
