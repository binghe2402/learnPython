from typing import List


class Solution:
    # # 遍历不同边界（宽度），根据最小高度
    # def largestRectangleArea(self, heights: List[int]) -> int:
    #     area = 0
    #     for i in range(len(heights)):
    #         for j in range(i, len(heights)):
    #             area = max(area, (j-i+1)*min(heights[i:j+1]))
    #     return area

    # 遍历不同高度(从每个柱向两侧扩展)，根据当前高度的最小宽度（最窄边界）
    # 当两侧高度小于中央开始起点的高度，即为边界
    def largestRectangleArea(self, heights: List[int]) -> int:
        area = 0
        for i in range(len(heights)):
            left = right = i
            # 寻找左边界
            while left >= 0 and heights[i] <= heights[left]:
                left -= 1
            # 寻找右边界
            while right < len(heights) and heights[i] <= heights[right]:
                right += 1
            area = max(area, (right - left - 1)*heights[i])
        return area
