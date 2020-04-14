from p445_add_two_number_II import ListNode, Solution

input1 = [7, 2, 4, 3]
input2 = [5, 6, 4]


def stringToListNode(input):
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
    l1 = stringToListNode(input1)
    l2 = stringToListNode(input2)
    ret = Solution().addTwoNumbers(l1, l2)
    out = listNodeToString(ret)
    print(out)


if __name__ == '__main__':
    main()
