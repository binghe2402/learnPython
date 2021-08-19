from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def __init__(self):
        self.res = []
        self.deep = 0

    def rightSideView(self, root: TreeNode) -> List[int]:
        if root:
            if len(self.res) <= self.deep:
                self.res.append(root.val)
            if root.right:
                self.deep += 1
                self.rightSideView(root.right)
                self.deep -= 1
            if root.left:
                self.deep += 1
                self.rightSideView(root.left)
                self.deep -= 1
        return self.res


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


def main():

    root = stringToTreeNode(line)

    ret = Solution().rightSideView(root)

    print(ret)


if __name__ == '__main__':
    line = '[1,2,3,4]'
    main()
