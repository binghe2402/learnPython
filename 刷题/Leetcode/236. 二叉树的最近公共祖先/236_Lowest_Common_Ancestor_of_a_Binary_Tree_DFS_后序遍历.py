# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        '''
        搜索从根节点开始搜索，访问左右支，
        如果遇到终止条件就终止并返回。
        p或q就向上返回该节点，越过叶子节点遇到None就向上返回None。

        如果某个节点的左子树和右子树均有返回值，则该节点就是要找的。
        如果某个节点本身是p或q，以及左支或右支有返回值，那也是。
        这个算法并不需要O(N^2)，而是O(N)。
        不需要对于每层节点都来一次递归搜索，
        而是一路向下访问到终止条件，然后一路向上返回，汇总在每个节点处进行判断。
        也就是后序遍历：访问左支，访问右支，访问节点。

        判断终止条件不能叫访问节点吧，所以应该不算前序遍历

        注意这里利用了题目条件，p和q一定存在，
        所以当返回到根节点，如果左右子树只有一个有返回值，
        那说明一定是q是p的子节点（或者反过来）

        '''
        son = {p, q}  # 这样一来不存在先找到p还是先找到q的问题，用集合的意义就不大了，直接判断两个相等即可。
        if root is None or root in son:
            return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        if left and right:
            return root
        # elif left:
        #     return left
        # elif right:
        #     return right
        # else:
        #     return None
        # 这三种情况可以合并为
        else:
            return left or right
