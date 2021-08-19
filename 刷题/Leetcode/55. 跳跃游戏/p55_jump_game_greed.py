from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        max_dst = 0
        for i in range(n):
            if max_dst < i:
                return False
            max_dst = max(nums[i]+i, max_dst)
            if max_dst >= n-1:
                return True


s = Solution()
a = [3, 2, 1, 0, 4]
res = s.canJump(a)
print(res)
