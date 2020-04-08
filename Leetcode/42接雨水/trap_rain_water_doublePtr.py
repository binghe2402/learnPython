from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        water = 0
        if not height:
            return water
        left_max, right_max = height[0], height[-1]
        i, j = 0, len(height)-1
        while i < j:
            if left_max < right_max:
                water += left_max - height[i]
                i += 1
                left_max = max(height[i], left_max)
            else:
                water += right_max - height[j]
                j -= 1
                right_max = max(height[j], right_max)
        return water


height = [0, 1, 0, 2, 1]
s = Solution()
water = s.trap(height)
print(water)
