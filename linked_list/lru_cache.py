class node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class lru:
    def __init__(self, capacity):
        self.capacity = capacity
        self.map = {}
        self.left = node(0, 0)   # LRU end
        self.right = node(0, 0)  # MRU end
        self.left.next = self.right
        self.right.prev = self.left

    def _remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def _insert(self, node):
        last = self.right.prev
        last.next = node
        node.prev = last
        node.next = self.right
        self.right.prev = node

    def get(self, key):
        if key not in self.map:
            return -1
        node = self.map[key]
        self._remove(node)
        self._insert(node)
        return node.val

    def put(self, key, val):
        if key in self.map:
            self._remove(self.map[key])
        new_node = node(key, val)
        self.map[key] = new_node
        self._insert(new_node)

        if len(self.map) > self.capacity:
            lru_node = self.left.next
            self._remove(lru_node)
            del self.map[lru_node.key]
