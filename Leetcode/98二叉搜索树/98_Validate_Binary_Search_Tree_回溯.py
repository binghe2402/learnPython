# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        min_val = -float('inf')
        max_val = float('inf')

        def backtrack(node, min_val, max_val):
            res = True
            if node.left and res:
                res = min_val < node.left.val < node.val \
                    and backtrack(node.left, min_val, min(max_val, node.val))
            if node.right and res:
                res = node.val < node.right.val < max_val \
                    and backtrack(node.right, max(min_val, node.val), max_val)
            return res

        if root:
            return backtrack(root, min_val, max_val)
        else:
            return True
