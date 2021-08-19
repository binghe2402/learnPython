# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.s = 0

    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:

        def travalTree(node):
            if node is None:
                return
            if low <= node.val <= high:
                self.s += node.val
            if node.val >= low:
                travalTree(node.left)
            if node.val <= high:
                travalTree(node.right)
        travalTree(root)
        return(self.s)
