# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def dfs(root, son, track, path):
            if root and root not in path:
                track.append(root)
                if root in son:
                    son.remove(root)
                    return track
                if dfs(root.left, son, track, path) or dfs(root.right, son, track, path):
                    return track
                track.pop()
        son = {p, q}
        path = dfs(root, son, [], [])
        for t in path:
            if dfs(t.left, son, [], path) or dfs(t.right, son, [], path):
                return t
