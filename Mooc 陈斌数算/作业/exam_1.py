class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def buildTree(seq):
    tree = root = TreeNode(seq[0])

    def put(x, root):
        if x < root.val:
            if root.left:
                put(x, root.left)
            else:
                root.left = TreeNode(x)
        else:
            if root.right:
                put(x, root.right)
            else:
                root.right = TreeNode(x)

    for x in seq[1:]:
        put(x, root)
    return tree


# def printTree(root):
#     output = []
#     stack = []
#     while root or stack:
#         while root:
#             output.append(str(root.val))
#             stack.append(root)
#             root = root.left
#         root = stack.pop()
#         if root.right or root.left:
#             root = root.right
#         else:
#             print('->'.join(output))
#             if stack:
#                 output = output[:output.index(str(stack[-1].val))+1]
#             root = root.right


def printTree(root, output=[]):
    if root:
        output.append(str(root.val))
        if not(root.left or root.right):
            print('->'.join(output))
            output.pop()
            return

        printTree(root.left, output)
        printTree(root.right, output)
        output.pop()
        # output.pop()


if __name__ == "__main__":
    seq = list(map(int, input().split()))
    tree = buildTree(seq)
    printTree(tree)
