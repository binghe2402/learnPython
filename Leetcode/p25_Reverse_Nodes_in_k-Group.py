# Definition for singly-linked list.


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        def reverseListNode(head, tail):
            cur = head
            pre = tail.next
            while cur is not tail:
                cur.next, cur, pre = pre, cur.next, cur
            cur.next = pre
            return tail, head

        hair = ListNode(0)    # 关键在于hair节点的引入，使第一段也可以正常加入循环
        hair.next = head

        pretail = hair
        tail = pretail

        while head:
            for n in range(k):
                tail = tail.next
                if not tail:
                    head = tail
                    break
            else:
                head, tail = reverseListNode(head, tail)
                pretail.next = head
                pretail = tail
                head = tail.next
        return hair.next


def listToListNode(input):
    # Generate list from the input
    numbers = input

    # Now convert that list into linked list
    dummyRoot = ListNode(0)
    ptr = dummyRoot
    for number in numbers:
        ptr.next = ListNode(number)
        ptr = ptr.next

    ptr = dummyRoot.next
    return ptr


def listNodeToString(node):
    if not node:
        return "[]"

    result = ""
    while node:
        result += str(node.val) + ", "
        node = node.next
    return "[" + result[:-2] + "]"


def main():

    head = listToListNode(nums)

    ret = Solution().reverseKGroup(head, k)

    out = listNodeToString(ret)
    print(out)


nums = [1, 2, 3, 4, 5]
k = 2

if __name__ == '__main__':
    main()
