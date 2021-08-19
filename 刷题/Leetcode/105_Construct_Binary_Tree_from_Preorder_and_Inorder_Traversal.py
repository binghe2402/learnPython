from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if preorder:
            root = preorder[0]
            root_in_inorder = inorder.index(root)
            inorder_left = inorder[:root_in_inorder]
            inorder_right = inorder[root_in_inorder+1:]
            preorder_left = preorder[1:root_in_inorder+1]
            preorder_right = preorder[root_in_inorder+1:]
            tree = TreeNode(root)
            tree.left = self.buildTree(preorder_left, inorder_left)
            tree.right = self.buildTree(preorder_right, inorder_right)
            return tree
