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
        val = -float('inf')

        stack = []

        while stack or root:
            # 以每个节点左支为索引，逐层入栈，右支不入栈
            # 但一个节点的右支可能是右子树的左支的root，此时入栈了。它的身份是左支的root，而非右支。
            # 如果左支为None，则返回它的root，去寻找右支。
            # 如果右支为None，说明它的root的所有子树已经全部访问，返回上层。
            if root:
                stack.append(root)
                root = root.left
                continue
            root = stack.pop()
            if not root.val > val:
                return False
            val = root.val
            root = root.right
        return True
