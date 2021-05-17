from typing import List


class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        HIGH_BIT = max(nums).bit_length()     # 结果位数不会超过最大数的位数
        res = 0
        for k in range(HIGH_BIT, -1, -1):     # 从高位至低位进行计算
            aj = set()
            for n in nums:
                aj.add(n >> k)
            res = (res << 1) + 1
            found = False
            for ai in nums:
                if ((ai >> k) ^ res) in aj:
                    found = True
                    break
            if found is False:
                res -= 1
        return res


s = Solution()
nums = [2, 4]
res = s.findMaximumXOR(nums)
print(res)
