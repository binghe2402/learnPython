# Definition for singly-linked list.
from typing import List


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        lists = [ln for ln in lists if ln]
        new_ln = ListNode(None)
        cur = new_ln
        # print(lists)
        while lists:
            lists.sort(key=lambda ln: ln.val, reverse=1)
            cur.next = lists[-1]
            cur = cur.next
            lists[-1] = lists[-1].next
            if lists[-1] is None:
                lists.pop()
        return new_ln.next
