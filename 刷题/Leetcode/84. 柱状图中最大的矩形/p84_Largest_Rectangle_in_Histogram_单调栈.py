from typing import List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        left = [None]*len(heights)

        # 利用单调栈求得每个柱的左右边界
        # 以左边界为例
        # 从i开始向左寻找，当heights[letf]<heights[i]，即找到i的左边界
        # 因此维护单调栈，从左向右遍历，逐步将i加入栈中，
        # 并在每一个新的i,首先移除栈中>=heights[i]的i值
        # 移除后的栈顶就是左边界，即左侧第一个 < heighs[i]的值
        for i in range(len(heights)):
            # left 为i柱的左边界
            while stack and heights[i] <= heights[stack[-1]]:
                stack.pop()
            left[i] = stack[-1] if stack else -1
            stack.append(i)

        right = [None]*len(heights)
        stack = []
        for i in range(len(heights)):
            # right 为i柱的右边界
            j = len(heights)-i-1
            while stack and heights[j] <= heights[stack[-1]]:
                stack.pop()
            right[j] = stack[-1] if stack else len(heights)
            stack.append(j)

        area = max(
            (
                (right[i]-left[i]-1)*heights[i] for i in range(len(heights))
            )
        )
        return area
