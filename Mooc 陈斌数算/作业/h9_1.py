'''层序遍历表示的二叉树的中序遍历'''


class BinTreeNode:
    def __init__(self, root=None, left=None, right=None):
        self.val = root
        self.left = left
        self.right = right


def seq2tree(seq):
    tree = BinTreeNode(seq[0])
    stack = [tree]
    i = 1
    j = 0
    while i < len(seq):
        node = stack[j]
        j += 1
        if seq[i]:
            node.left = BinTreeNode(seq[i])
            stack.append(node.left)
        i += 1
        if not i < len(seq):
            break
        if seq[i]:
            node.right = BinTreeNode(seq[i])
            stack.append(node.right)
        i += 1
    return tree


def inorderTree(root):
    def find(root, res=[]):
        # # 递归法
        # if root:
        #     find(root.left, res)
        #     res.append(root.val)
        #     find(root.right, res)
        # else:
        #     return
        # return res

        # 栈法
        stack = []
        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            res.append(root.val)
            root = root.right
        return res

    # 中序遍历树
    return find(root)


lst = eval(input())
tree = seq2tree(lst)
inorder = inorderTree(tree)
print(('%s '*len(inorder)).strip() % tuple(i for i in inorder))
