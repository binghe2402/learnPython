# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# 按理说是O(N)吧，但是为啥这么慢呢

# 一通操作更慢了
# 尝试了下面搜索时把append去掉，也没有明显改善


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        track = []
        # def dfs(root, son, track, path):
        # 把可变对象假惺惺的当参数传进去有什么意义呢
        # 为什么不直接用全局对象
        # 还是有意义的，方便对不同的初值复用函数，方便返回值
        # 虽然下面这里的返回值本质上还是全局对象

        # def dfs(root, son, [], [])
        def dfs(root, p, q):
            if root:  # and root not in path:  没有必要在这检测是否访问过，在下面循环就可以了
                # 这里检测好像是开始想从下往上找交汇的时候的遗留，类似官方的记录父节点
                # track.append(root)   挪到下面，确认了再添加，就不用pop了
                # 这里注意，append挪到下面后，先调用dfs，再append，
                # 也就是深层的append先执行。所以记录的路径是倒序的，自下而上。
                # if root in son:
                    # son.remove(root)    # 这里不remove应该也行，题目要求了不会重复
                if root == p or root == q:
                    track.append(root)
                    return True
                # if dfs(root.left, son, track, path) or dfs(root.right, son, track, path):
                if dfs(root.left, p, q) or dfs(root.right, p, q):
                    track.append(root)
                    return True
                # track.pop()
            return False
        # son = {p, q}
        track = []
        # path = dfs(root, son, [], [])
        dfs(root, p, q)
        path = track[:]
        # 实际上由于下面的搜索不需要记录，完全可以把append去掉，这样也不需要再加一个path了
        # 唯一的缺点是上面的dfs不能复用，
        # for t in path[:-1]:
        for t in path[1:]:     # 倒序了
            # if dfs(t.left, son, [], path) or dfs(t.right, son, [], path):
                # 左支可以不用搜索，如果右支完全没找到，那就一定是path[-1],
                # 也就是q在p的子树上。（假设先找到p）因为p,q一定存在
            # if dfs(t.right, son, [], path):
            if t.right not in path and dfs(t.right, p, q):
                return t
        return path[0]
