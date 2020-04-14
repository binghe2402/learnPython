# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        def reserveListNode(head):
            pre = None
            cur = head
            while cur:
                cur.next, pre, cur = pre, cur, cur.next
            return pre

        l1 = reserveListNode(l1)
        l2 = reserveListNode(l2)

        cl1, cl2 = l1, l2

        carry = 0

        # 为了节省内存不引入新的链表，因此后面感觉有点臃肿

        while cl1.next and cl2.next:
            cl1.val += (cl2.val + carry)
            carry, cl1.val = divmod(cl1.val, 10)
            cl1, cl2 = cl1.next, cl2.next
        else:
            cl1.val += (cl2.val + carry)
            carry, cl1.val = divmod(cl1.val, 10)

            cl1.next = cl1.next or cl2.next

            if cl1.next:
                cl1 = cl1.next
                while cl1 and cl1.next:
                    carry, cl1.val = divmod(cl1.val+carry, 10)
                    cl1 = cl1.next
                else:
                    carry, cl1.val = divmod(cl1.val+carry, 10)

            if carry:
                cl1.next = ListNode(carry)

        return reserveListNode(l1)
