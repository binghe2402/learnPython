from typing import List
from functools import reduce


class Solution:
    def singleNumbers(self, nums: List[int]) -> List[int]:
        res = reduce(lambda x, y: x ^ y, nums)
        i = 1
        while not (i & res):
            i <<= 1
        res1 = res2 = 0
        for n in nums:
            if i & n:
                res1 = res1 ^ n
            else:
                res2 = res2 ^ n
        return [res1, res2]


nums = [1, 2, 5, 2]
s = Solution()
res = s.singleNumbers(nums)
print(res)
