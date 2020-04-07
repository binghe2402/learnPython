from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        water = [None]*len(height)
        h = sorted(enumerate(height), key=lambda x: -x[1])
        for k in h:
            for i in range(min(k[0], h[0][0]), max(k[0], h[0][0])+1):
                if water[i] is None:
                    water[i] = k[1]-height[i]

        # 计算最高和次高之间的水，然后计算最高和3高之间的水。
        # 相应跳过重复部分。
        # 3高水位低与次高，所以3高和最高之间的位置若有重合，水位一定低于次高水位，可直接跳过。

        return sum(water)


height = [5, 2, 1, 2, 1, 5]
s = Solution()
water = s.trap(height)
print(water)
