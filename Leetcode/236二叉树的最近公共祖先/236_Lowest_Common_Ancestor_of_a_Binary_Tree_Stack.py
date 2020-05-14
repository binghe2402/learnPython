'''
还不对
'''
'''
好像不行
'''

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        son = {p, q}
        stack = []
        while son and root or stack:
            if root:
                if root in son:
                    son.remove(root)
                else:
                    stack.append(root)
                    root = root.left
                continue
            root = stack.pop().right
        return root
