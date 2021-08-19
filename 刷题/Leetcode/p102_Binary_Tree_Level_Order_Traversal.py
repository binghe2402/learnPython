from typing import List
# Definition for a binary tree node.


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if root is None:
            return []
        levelList = [[root]]
        res = [[root.val]]
        while levelList[-1]:
            levelList.append([])
            res.append([])
            for node in levelList[-2]:
                if node.left:
                    levelList[-1].append(node.left)
                    res[-1].append(node.left.val)
                if node.right:
                    levelList[-1].append(node.right)
                    res[-1].append(node.right.val)
        return res[:-1]
