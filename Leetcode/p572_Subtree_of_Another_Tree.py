# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        # self.flag = False

        def check(s, t):
            if s is None and t is None:
                return True
            elif bool(s) ^ bool(t):
                return False
            else:
                return s.val == t.val \
                    and check(s.left, t.left) \
                    and check(s.right, t.right)

        stack = []
        while stack or s:
            if s:
                if check(s, t):
                    return True
                stack.append(s)
                s = s.left
                continue
            s = stack.pop()
            s = s.right
        return False
