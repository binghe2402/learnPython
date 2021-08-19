from typing import List


class Solution:
    def shipWithinDays(self, weights: List[int], D: int) -> int:
        left, right = max(weights), sum(weights)

        def check(x):
            d = 1
            cur_w = 0
            for w in weights:
                if cur_w+w > x:
                    d += 1
                    cur_w = 0
                cur_w += w
            return d <= D
        while left < right:
            mid = left+(right-left)//2
            if check(mid):
                right = mid
            else:
                left = mid + 1
        return left
