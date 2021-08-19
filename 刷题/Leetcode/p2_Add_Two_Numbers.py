# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        carry = 0
        hair = ListNode()
        res = hair
        while l1 and l2:
            add = l1.val + l2.val + carry
            res.next = ListNode(add % 10)
            res = res.next
            carry = add//10
            l1, l2 = l1.next, l2.next
        l1 = l1 or l2
        while l1:
            add = l1.val + carry
            res.next = ListNode(add % 10)
            res = res.next
            carry = add//10
            l1 = l1.next
        if carry:
            res.next = ListNode(carry)
        return hair.next
