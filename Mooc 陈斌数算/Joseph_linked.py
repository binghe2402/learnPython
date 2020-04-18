class Node:
    def __init__(self, x):
        self.val = x
        self.next = None
        self.pre = None


n = int(input())
m = int(input())
head = Node(0)
cur = head
for i in range(1, n):
    cur.next = Node(i)
    cur.next.pre = cur
    cur = cur.next
cur.next = head
head.pre = cur
lst = []

while head != head.next:
    for i in range(m-1):
        head = head.next
    lst.append(head.val)
    head.pre.next = head.next
    head.next.pre = head.pre
    head = head.next
else:
    lst.append(head.val)

print(lst)
