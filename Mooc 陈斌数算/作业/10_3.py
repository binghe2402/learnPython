class BinTreeNode:
    def __init__(self, root=None, left=None, right=None):
        self.val = root
        self.left = left
        self.right = right


def buildTree(seq):
    tree = root = BinTreeNode(seq[0])

    def put(root, x):
        while root:
            if x > root.val:
                if root.right:
                    root = root.right
                else:
                    root.right = BinTreeNode(x)
                    break
            else:
                if root.left:
                    root = root.left
                else:
                    root.left = BinTreeNode(x)
                    break
        else:
            root = BinTreeNode(x)
        return root
    for x in seq[1:]:
        put(root, x)
    return tree


def changeTree(root, seq):
    if root:
        root.val = sum([x for x in seq if x >= root.val])
        changeTree(root.left, seq)
        changeTree(root.right, seq)


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
changeTree(tree, seq)
levelorder = levelorderTree(tree)
# print(('%s '*len(levelorder)).strip() % tuple(i for i in levelorder))
print(*levelorder)
