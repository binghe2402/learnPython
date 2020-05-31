import random


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


res_rec = []
res_itr = []


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


def printTree_Iterate(root):
    output = []
    stack = []
    while root or stack:
        while root:
            output.append(str(root.val))
            stack.append(root)
            root = root.left
        root = stack.pop()
        if root.right or root.left:
            root = root.right
        else:
            res_itr.append('->'.join(output))
            if stack:
                output = output[:output.index(str(stack[-1].val))+1]
            root = root.right


def printTree_Recursive(root, output=[]):
    if root:
        output.append(str(root.val))
        if not(root.left or root.right):
            res_rec.append('->'.join(output))
        printTree_Recursive(root.left, output)
        printTree_Recursive(root.right, output)
        output.pop()
        # output.pop()


if __name__ == "__main__":
    # seq = random.sample(range(100), random.randint(1, 10))
    seq = [11, 48, 15, 70, 69, 13]
    tree = buildTree(seq)
    printTree_Recursive(tree)
    printTree_Iterate(tree)
    if res_rec != res_itr:
        print(seq)
        print(res_rec)
        print(res_itr)
