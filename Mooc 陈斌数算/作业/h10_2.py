class BinTreeNode:
    def __init__(self, root=None, left=None, right=None):
        self.val = root
        self.left = left
        self.right = right


def buildTree(seq):
    seq.sort(reverse=True)

    def struct(n):
        node = [BinTreeNode()]
        i = 0
        while len(node) < n:
            node[i].left = BinTreeNode()
            node.append(node[i].left)
            if not len(node) < n:
                break
            node[i].right = BinTreeNode()
            node.append(node[i].right)
            i += 1
        return node[0]

    def fill(root, seq):
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
    return fill(struct(len(seq)), seq)


def levelorderTree(root):
    node_list = [root]
    res = []
    for node in node_list:
        if node:
            res.append(node.val)
            node_list.append(node.left)
            node_list.append(node.right)
    return res


seq = list(map(int, input().split()))
tree = buildTree(seq)
levelorder = levelorderTree(tree)
# print(('%s '*len(levelorder)).strip() % tuple(i for i in levelorder))
print(*levelorder)
