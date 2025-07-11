from collections import OrderedDict

# LRU cache using OrderedDict for O(1) get and put

class lru:
    def __init__(self, capacity):
        self.capacity = capacity
        self.map = OrderedDict()

    def get(self, key):
        if key not in self.map:
            return -1
        self.map.move_to_end(key)
        return self.map[key]

    def put(self, key, val):
        if key in self.map:
            self.map.move_to_end(key)
        self.map[key] = val
        if len(self.map) > self.capacity:
            self.map.popitem(last=False)

# OrderedDict maintains insertion order
# move_to_end(key) makes key most recently used
# popitem(last=False) removes least recently used key

# Setup example
cache = lru(2)
cache.put(1, 1)
cache.put(2, 2)
print(cache.get(1))    # 1
cache.put(3, 3)        # evicts key 2
print(cache.get(2))    # -1
cache.put(4, 4)        # evicts key 1
print(cache.get(1))    # -1
print(cache.get(3))    # 3
print(cache.get(4))    # 4
