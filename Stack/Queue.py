# class Queue:
#     def __init__(self):
#         self.items = []

#     def isEmpty(self):
#         return self.items == []

#     def push(self, item):
#         self.items.insert(0,item)

#     def get(self):
#         return self.items.pop()

#     def size(self):
#         return len(self.items)

class Node:
    def init(self, item):
        self.item = item
        self.next = None


class Queue:
    def init(self):
        self.head = None
        self.last = None
        self.len = 0
    
    def size(self):
        return self.len

    def enqueue(self, item):
        node = Node(item)
        if not self.last:
            self.head = node
        else:
            self.last.next = node
            self.last = node
        self.len += 1

    def dequeue(self):
        if self.head != self.last:
            # Has at least two elements
            res = self.head
            self.head = self.head.next
            self.len -= 1
            return res
        # Has one or zero element
        res = self.head
        self.head = None
        self.last = None
        self.len -= 1
        return res