from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ans = 0
        maximum = nums[0]
        for i in range(len(nums)):
            if ans > 0:
                ans += nums[i]
            else:
                ans = nums[i]
            maximum = max(ans, maximum)
        return maximum
