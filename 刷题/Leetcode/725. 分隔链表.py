from typing import List


class ListNode:
    # Definition for singly-linked list.
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class ListNode:
    # Definition for singly-linked list.
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def splitListToParts(self, head: ListNode, k: int) -> List[ListNode]:
        cur = head
        length = 0
        while cur:
            length += 1
            cur = cur.next

        l1, l2 = divmod(length, k)

        cur = head
        res = []
        for i in range(l2):
            res.append(cur)
            # cur = cur.next
            for j in range(l1):
                # res[-1].append(cur)
                cur = cur.next
            temp = cur.next
            cur.next = None

            cur = temp

        for i in range(k-l2):
            if cur:
                res.append(cur)
                for j in range(l1-1):
                    cur = cur.next
                temp = cur.next
                cur.next = None
                cur = temp
            else:
                res.append(None)

        return res
