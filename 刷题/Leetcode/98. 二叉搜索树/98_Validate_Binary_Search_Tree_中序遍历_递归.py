# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


'''
可以发现，有效的二叉搜索树的中序遍历一定是升序的，因此利用这个特点直接做中序遍历
'''


class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        self.val = -float('inf')

        def helper(root):
            if root is None:
                return True
            if not helper(root.left):
                return False
            if not root.val > self.val:
                return False
            self.val = root.val
            return helper(root.right)

        return helper(root)
