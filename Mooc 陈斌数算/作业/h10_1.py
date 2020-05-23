'''二叉查找树填空'''


class BinTreeNode:
    def __init__(self, root=None, left=None, right=None):
        self.val = root
        self.left = left
        self.right = right


def buildTree(N, SN):
    # # 根据输入节点结构生成  更改编号方式就会失效 只有按照前序遍历顺序输入节点结构才行
    # stack = []
    # tree = root = BinTreeNode(0, *SN[0])
    # i = 1
    # while i < N:
    #     if type(root.left) is int:
    #         stack.append(root)
    #         root.left = BinTreeNode(0, *SN[i])
    #         root = root.left
    #         i += 1
    #         continue
    #     if type(root.right) is int:
    #         root.right = BinTreeNode(0, *SN[i])
    #         root = root.right
    #         i += 1
    #         continue
    #     root = stack.pop()
    # return tree

    # 根据节点编号关系生成
    node = [BinTreeNode(i) for i in range(N)]
    for i in range(N):
        if SN[i][0]:
            node[i].left = node[SN[i][0]]
        if SN[i][1]:
            node[i].right = node[SN[i][1]]
    return node[0]


def fillTree(root, seq):
    # # 递归 中序遍历
    # if root:
    #     fillTree(root.left, seq)
    #     root.val = seq.pop()
    #     fillTree(root.right, seq)
    # return root

    # 栈
    stack = []
    tree = root
    while root or stack:
        while root:
            stack.append(root)
            root = root.left
        root = stack.pop()
        root.val = seq.pop()
        root = root.right
    return tree


def levelorderTree(root):
    node_list = [root]
    res = []
    for node in node_list:
        if node:
            res.append(node.val)
            node_list.append(node.left)
            node_list.append(node.right)
    return res


N = int(input())
SN = [[0, 0] for i in range(N)]
for i in range(len(SN)):
    SN[i] = tuple(map(lambda x:
                      int(x) if x != '-1' else None,
                      input().split()))
seq = sorted(map(int, input().split()), reverse=True)
tree = buildTree(N, SN)
fillTree(tree, seq)
levelorder = levelorderTree(tree)
# print(('%s '*len(levelorder)).strip() % tuple(i for i in levelorder))
print(*levelorder)

'''
9
1 6
2 3
-1 -1
-1 4
5 -1
-1 -1
7 -1
-1 8
-1 -1
73 45 11 58 82 25 67 38 42
'''
