# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.hairNode = self.resNode = TreeNode(0)

    def increasingBST(self, root: TreeNode) -> TreeNode:
        # hairNode = resNode = TreeNode(0)
        self.TravelTree(root)
        return self.hairNode.right

    def TravelTree(self, node):
        if node is None:
            return
        self.TravelTree(node.left)
        # nonlocal resNode
        self.resNode.right = node
        node.left = None
        self.resNode = node
        self.TravelTree(node.right)


def stringToTreeNode(input):
    input = input.strip()
    input = input[1:-1]
    if not input:
        return None

    inputValues = [s.strip() for s in input.split(',')]
    root = TreeNode(int(inputValues[0]))
    nodeQueue = [root]
    front = 0
    index = 1
    while index < len(inputValues):
        node = nodeQueue[front]
        front = front + 1

        item = inputValues[index]
        index = index + 1
        if item != "null":
            leftNumber = int(item)
            node.left = TreeNode(leftNumber)
            nodeQueue.append(node.left)

        if index >= len(inputValues):
            break

        item = inputValues[index]
        index = index + 1
        if item != "null":
            rightNumber = int(item)
            node.right = TreeNode(rightNumber)
            nodeQueue.append(node.right)
    return root


def treeNodeToString(root):
    if not root:
        return "[]"
    output = ""
    queue = [root]
    current = 0
    while current != len(queue):
        node = queue[current]
        current = current + 1

        if not node:
            output += "null, "
            continue

        output += str(node.val) + ", "
        queue.append(node.left)
        queue.append(node.right)
    return "[" + output[:-2] + "]"


def main():

    root = stringToTreeNode(line)

    ret = Solution().increasingBST(root)

    print(treeNodeToString(ret))


if __name__ == '__main__':
    # line = '[5,1,7]'
    line = '[5,3,6,2,4,null,8,1,null,null,null,7,9]'
    main()
