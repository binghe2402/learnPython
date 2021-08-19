class Solution:
    def lengthOfLIS(self, nums) -> int:
        if len(nums) < 2:
            return len(nums)
        length = len(nums)
        dp = []
        for i in range(length):
            dp.append(1)
            for j in range(i):
                if nums[i] > nums[j] and dp[i] <= dp[j]:
                    dp[i] = dp[j]+1

        return max(dp)


s = Solution()
ss = [1, 3, 6, 7, 9, 4, 10, 5, 6]

print(s.lengthOfLIS(ss))
