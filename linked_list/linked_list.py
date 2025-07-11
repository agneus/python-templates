# Singly linked list implementation

class node:
    def __init__(self, val):
        self.val = val
        self.next = None

class linkedlist:
    def __init__(self):
        self.head = None

    def insert_head(self, val):
        new = node(val)
        new.next = self.head
        self.head = new

    def insert_tail(self, val):
        new = node(val)
        if not self.head:
            self.head = new
            return
        cur = self.head
        while cur.next:
            cur = cur.next
        cur.next = new

    def delete(self, val):
        if not self.head:
            return
        if self.head.val == val:
            self.head = self.head.next
            return
        cur = self.head
        while cur.next and cur.next.val != val:
            cur = cur.next
        if cur.next:
            cur.next = cur.next.next

    def traverse(self):
        cur = self.head
        result = []
        while cur:
            result.append(cur.val)
            cur = cur.next
        return result
