# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        level = [root]
        new_level = []
        xy = (x, y)
        for node in level:
            if node:

                new_level.append(node.left)
