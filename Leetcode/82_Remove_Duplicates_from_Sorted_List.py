# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if head is None:
            return
        hair = ListNode(None)
        hair.next = head
        pre, cur, nxt = hair, head, head.next

        while cur and nxt:
            if nxt.val == cur.val:
                pre.next = nxt.next
                cur.next = nxt.next
                nxt = cur.next
            else:
                if pre.next is cur:
                    pre = pre.next
                cur, nxt = cur.next, nxt.next
        return hair.next
