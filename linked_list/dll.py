class node:
    def __init__(self, val):
        self.val = val
        self.prev = None
        self.next = None

class dll:
    def __init__(self):
        self.left = None
        self.right = None
    
    def insert_left(self, val):
        new = node(val)
        new.next = self.left
        if self.left:
            self.left.prev = new
        self.left = new
        if not self.right:
            self.right = new

    def insert_right(self, val):
        new = node(val)
        new.prev = self.right
        if self.right:
            self.right.next = new
        self.right = new
        if not self.left:
            self.left = new

    def delete(self, val):
        cur = self.left
        while cur and cur.val != val:
            cur = cur.next
        if not cur:
            return
        if cur.prev:
            cur.prev.next = cur.next
        else:
            self.left = cur.next
        if cur.next:
            cur.next.prev = cur.prev
        else:
            self.right = cur.prev
        
    def traverse_forward(self):
        cur = self.left
        result = []
        while cur:
            result.append(cur.val)
            cur = cur.next
        return result

    def traverse_backward(self):
        cur = self.right
        result = []
        while cur:
            result.append(cur.val)
            cur = cur.prev
        return result