# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        def readNum(ln):
            if ln:
                num = 0
                while ln:
                    # 此处对biginteger做乘法是较大开销
                    num = 10*num+ln.val
                    ln = ln.next
            return num

        new_num = str(readNum(l1)+readNum(l2))
        new_l = ListNode(int(new_num[0]))
        ptr = new_l
        for d in new_num[1:]:
            ptr.next = ListNode(int(d))
            ptr = ptr.next

        return new_l
