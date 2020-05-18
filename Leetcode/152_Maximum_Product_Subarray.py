from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        '''原始dp
        dp = [[-float('inf'), float('inf')] for i in range(len(nums))]
        dp[0] = [nums[0], nums[0]]

        # dp[i]为以nums[i]结尾的子数组中的最大和最小

        for i in range(1, len(nums)):
            dp[i][0] = max(dp[i-1][0]*nums[i], dp[i-1][1]*nums[i], nums[i])
            dp[i][1] = min(dp[i-1][0]*nums[i], dp[i-1][1]*nums[i], nums[i])
        return max([x[0] for x in dp])
        '''
        '''空间优化
        max_value, min_value, max_res = nums[0], nums[0], nums[0]
        for i in range(1, len(nums)):
            max_value, min_value = \
                max(max_value*nums[i], min_value*nums[i], nums[i]),\
                min(max_value*nums[i], min_value*nums[i], nums[i])
            max_res = max(max_res, max_value)
        return max_res
        '''
        '''根据nums[i]的正负号选取计算合适的最大值和最小值计算，减少乘法次数
        容易知道，
        当nums[i]为正，新的最大值最小值由原来的最大值最小值*nums[i]得到。
        当nums[i]为负，应交换最大值和最小。
        注意由于还要对得到的结果做max/min,所以先交换再计算。
        
        或者直接根据得到的max_value和min_value的大小关系交换
        '''
        max_value, min_value, max_res = nums[0], nums[0], nums[0]
        for i in range(1, len(nums)):
            if nums[i] < 0:
                max_value, min_value = min_value, max_value
            max_value, min_value = \
                max(max_value*nums[i], nums[i]),\
                min(min_value*nums[i], nums[i])
            max_res = max(max_res, max_value)
        return max_res


nums = [-4, -3, -2]
s = Solution()
res = s.maxProduct(nums)
print(res)
