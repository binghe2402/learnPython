# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        def check(root1, root2):
            if root1 is None and root2 is None:
                return True
            elif root1 and root2:
                if root1.val == root2.val:
                    return check(root1.left, root2.right) and check(root1.right, root2.left)
            else:
                return False
        return check(root, root)
