# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        def readNum(ln):
            stack = []
            while ln:
                stack.append(ln.val)
                ln = ln.next
            return stack

        num1, num2 = readNum(l1), readNum(l2)
        rise = 0
        new_num = None
        while num1 or num2 or rise:
            x = num1.pop() if num1 else 0
            y = num2.pop() if num2 else 0
            rise, d = divmod(x+y+rise, 10)
            nxt = new_num
            new_num = ListNode(d)
            new_num.next = nxt

        return new_num

