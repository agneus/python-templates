# Doubly linked list implementation

class node:
    def __init__(self, val):
        self.val = val
        self.prev = None
        self.next = None

class dll:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_head(self, val):
        new = node(val)
        new.next = self.head
        if self.head:
            self.head.prev = new
        self.head = new
        if not self.tail:
            self.tail = new

    def insert_tail(self, val):
        new = node(val)
        new.prev = self.tail
        if self.tail:
            self.tail.next = new
        self.tail = new
        if not self.head:
            self.head = new

    def delete(self, val):
        cur = self.head
        while cur and cur.val != val:
            cur = cur.next
        if not cur:
            return
        if cur.prev:
            cur.prev.next = cur.next
        else:
            self.head = cur.next
        if cur.next:
            cur.next.prev = cur.prev
        else:
            self.tail = cur.prev

    def traverse_forward(self):
        cur = self.head
        result = []
        while cur:
            result.append(cur.val)
            cur = cur.next
        return result

    def traverse_backward(self):
        cur = self.tail
        result = []
        while cur:
            result.append(cur.val)
            cur = cur.prev
        return result
