from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        dp = [0]*len(nums)
        dp[0] = nums[0]
        for i in range(1, len(nums)):

            # dp[i] 表示 以 第i个数结尾的 那些连续子数组的 最大和
            # 如， dp[4]表示，nums[0:4+1],nums[1:4+1],nums[2:4+1],nums[3:4+1],nums[4:4+1],中的最大和

            dp[i] = max(dp[i-1]+nums[i], nums[i])

        return max(dp)
