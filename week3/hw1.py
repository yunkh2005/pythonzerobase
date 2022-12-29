class Node:
    def __init__(self, data, prev=None, next=None):
        self.data = data
        self.prev = prev
        self.next = next

class LinkedQueue:
    def __init__(self):
        self.front = None
        self.rear = None

    def is_empty(self):
        if self.front == None:
            return True
        else:
            return False

    def put(self, data):
        if self.front == None:
            self.front = Node(data)
            self.rear = self.front
        else:
            node = self.front
            while node.next:
                node = node.next
            new = Node(data)
            node.next = new
            new.prev = node
            self.rear = new

    def get(self):
        node = self.front
        while node:
            print(node.data, end=' ')
            node = node.next
            self.front = None
            

    def peek(self):
        node = self.front
        while node:
            print(node.data, end=' ')
            node = node.next

# Test code
queue = LinkedQueue()

print(queue.is_empty())             # True
for i in range(10):
    queue.put(i)
print(queue.is_empty())             # False

for _ in range(11):
    print(queue.get(), end=' ')     # 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, None
print()

for i in range(20):
    queue.put(i)
print(queue.is_empty())             # False

for _ in range(5):
    print(queue.peek(), end=' ')    # 0, 1, 2, 3, 4
print()

for _ in range(21):
    print(queue.get(), end=' ')     # 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, None
print()
print(queue.is_empty())             # True