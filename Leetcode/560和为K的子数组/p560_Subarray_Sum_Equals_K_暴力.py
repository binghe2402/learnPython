from typing import List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        cnt = 0
        for i in range(len(nums)):
            summary = 0
            for j in range(i, len(nums)):
                summary += nums[j]
                if summary == k:
                    cnt += 1
        return cnt
