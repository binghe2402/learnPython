'''嵌套列表表示的N叉树的后序遍历'''


def postorderTree(tree, postorder=[]):
    if len(tree) > 1:
        for node in tree[1:]:
            postorderTree(node)
    postorder.append(tree[0])
    return postorder


tree = eval(input())
postorder = postorderTree(tree)
print(('%s '*len(postorder)).strip() % tuple(i for i in postorder))
