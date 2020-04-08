from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        water = 0
        if not height:
            return water
        stack = []

        for h in range(len(height)):
            while stack and height[h] > height[stack[-1]]:
                bottom = stack.pop()

                if stack:
                    d = h - stack[-1] - 1
                    water += d * \
                        (min(height[stack[-1]], height[h])-height[bottom])
            else:
                stack.append(h)
        return water


height = [4, 2, 0, 3, 2, 5]
s = Solution()
water = s.trap(height)
print(water)
