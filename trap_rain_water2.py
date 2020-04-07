from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        water = [0]*len(height)
        for i in range(1, len(height)):
            water[i] =

        return sum(water)


height = [5, 2, 1, 2, 1, 5]
s = Solution()
water = s.trap(height)
print(water)
