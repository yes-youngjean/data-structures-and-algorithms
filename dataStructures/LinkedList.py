class Node:
    def __init__(self, data):
            self.data = data
            self.next = None

a = Node(1)
b = Node(2)
c = Node(3)

a.next = b
b.next = c

current = a

while current:
    print(current.data)
    current = current.next

# 1, 2, 3
