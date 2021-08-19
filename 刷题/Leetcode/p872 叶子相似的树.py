# Definition for a binary tree node.
from typing import no_type_check


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        def getLeaves(tree):
            leaves = []
            stack = []
            node = tree
            while node or stack:
                while node:
                    stack.append(node)
                    node = node.left
                node = stack.pop()
                if not node.left and not node.right:
                    leaves.append(node.val)
                node = node.right
            return leaves
        return getLeaves(root1) == getLeaves(root2)
