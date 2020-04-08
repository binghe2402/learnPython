from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        water = 0
        if not height:
            return water
        left_max = [height[0]]
        right_max = [height[-1]]
        n = len(height)
        for i in range(1, n):
            left_max.append(max(height[i], left_max[-1]))
            right_max.insert(0, max(height[n-i-1], right_max[0]))

        for i in range(n):
            water += min(left_max[i], right_max[i])-height[i]
        return water


height = [0, 3, 0, 2, 4]
s = Solution()
water = s.trap(height)
print(water)
