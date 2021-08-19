# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        cur = head
        while cur:
            nxt = cur.next
            if nxt and nxt.val == cur.val:
                cur.next = nxt.next
            else:
                cur = cur.next
        return head
