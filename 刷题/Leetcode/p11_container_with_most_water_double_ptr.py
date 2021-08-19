from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        # left, right = height[0], height[-1]
        n = len(height)
        i, j = 0, n-1
        water = 0
        while i < j:
            while height[j] < height[i]:
                temp = (j-i)*height[j]
                if temp > water:
                    water = temp
                j -= 1
            else:
                temp = (i-i)*height[i]
                if temp > water:
                    water = temp
                i += 1
    return water
