class PriorityQueue:
    min_heap = []
    index1 = -1
    index2 = -1
    def __init__(self):
        pass

    def is_empty(self):
        if self.min_heap is None:
            return True
        else:
            return False

    def put(self, data):
        self.min_heap.append(data)
        self.min_heap.sort()      # 우선순위로 정렬

    def get(self):
        try:
            print(self.index1, end=' ')
            self.index1 += 1
            if self.index1 == 0:
                return self.min_heap[0][1]
            else:
                self.min_heap.pop(0)
                return self.min_heap[0][1]
        except:
            return None

    def peek(self):
        try:
            print(self.index2, end=' ')
            self.index2 += 1
            return self.min_heap[self.index2][1]
        except:
            return None

# Test code
pq = PriorityQueue()
pq.put((0, 'a'))
pq.put((5, 'b'))
pq.put((2, 'c'))
pq.put((1, 'd'))
pq.put((3, 'e'))
pq.put((4, 'f'))
print(pq.min_heap)
print(pq.peek())
print(pq.peek())
print(pq.peek())
print(pq.peek())
print(pq.peek())
print(pq.peek())
print()
print(pq.get())
print(pq.get())
print(pq.get())
print(pq.get())
print(pq.get())
print(pq.get())
print(pq.get())
