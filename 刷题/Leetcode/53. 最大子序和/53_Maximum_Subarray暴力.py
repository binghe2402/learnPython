from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxim = nums[0]
        for i in range(len(nums)):
            ans = 0
            for j in range(i, len(nums)):
                ans += nums[j]
                maxim = max(ans, maxim)
        return maxim
