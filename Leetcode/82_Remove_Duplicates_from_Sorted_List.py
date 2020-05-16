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
        pre, cur = hair, head

        while cur and cur.next:
            if cur.next.val == cur.val:
                while cur.next and cur.next.val == cur.val:
                    cur.next = cur.next.next
                pre.next = cur.next
            else:
                if pre.next is cur:
                    pre = pre.next

                cur = cur.next
        return hair.next
