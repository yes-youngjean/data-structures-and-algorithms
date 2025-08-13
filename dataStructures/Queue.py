class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Deque from empty queue")

    def peek(self):
        if self.is_empty():
            raise IndexError("Peek from empty queue")
        return self.items[0]

    def is_empty(self):
        return len(self.items) == 0

# =================================================================

from collections import deque
queue = deque()

queue.append(1)
queue.append(12)
# => [1,12]

print(queue.popleft())
print(queue[0])
print(not queue)  #Is it empty or not?