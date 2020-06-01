# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        stack = [[root]]
        for level in stack:
            if level:
                stack.append([])
            for node in level:
                if node:
                    stack[-1].append(node.left)
                    stack[-1].append(node.right)

            val_list = [node.val if node else None for node in stack[-1]]

            if list(reversed(val_list)) != val_list:
                return False
        return True
