class node:
    def __init__(self, val):
        self.val = val
        self.prev = None
        self.next = None

class dll:
    def __init__(self):
        self.left = node(0)   # dummy head
        self.right = node(0)  # dummy tail
        self.left.next = self.right
        self.right.prev = self.left

    def insert_right(self, val):
        new = node(val)
        last = self.right.prev
        last.next = new
        new.prev = last
        new.next = self.right
        self.right.prev = new

    def insert_left(self, val):
        new = node(val)
        first = self.left.next
        self.left.next = new
        new.prev = self.left
        new.next = first
        first.prev = new

    def delete(self, val):
        cur = self.left.next
        while cur != self.right:
            if cur.val == val:
                cur.prev.next = cur.next
                cur.next.prev = cur.prev
                return
            cur = cur.next

    def traverse(self):
        cur = self.left.next
        result = []
        while cur != self.right:
            result.append(cur.val)
            cur = cur.next
        return result
    
# usage
d = dll()
d.insert_right(10)
d.insert_left(5)
d.insert_right(15)
print(d.traverse())  # [5, 10, 15]
d.delete(10)
print(d.traverse())  # [5, 15]

