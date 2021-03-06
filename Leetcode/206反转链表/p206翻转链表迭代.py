# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        cur = head
        pre = None
        while cur:
            cur.next, cur, pre = pre, cur.next, cur
        return pre


def stringToListNode(input):
    # Generate list from the input
    numbers = (input)

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

    head = stringToListNode(line)

    ret = Solution().reverseList(head)

    out = listNodeToString(ret)
    print(out)


if __name__ == '__main__':
    line = [1, 2, 3, 4, 5]
    main()
