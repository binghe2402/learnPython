from typing import List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix = {0: 1}  # 对于前缀和刚好为k的情况，也就是summary-k刚好为0
        summary = 0
        cnt = 0
        for i in range(len(nums)):
            summary += nums[i]
            # 先查找summary-k，再赋值prefix[summary-k],防止当k=0重复计算
            if summary-k in prefix:
                cnt += prefix[summary-k]
            if summary in prefix:
                prefix[summary] += 1
            else:
                prefix[summary] = 1
        return cnt


s = Solution()
nums = [28, -28, 7, -70, 22, 65, -6]
k = 0
res = s.subarraySum(nums, k)
print(res)
