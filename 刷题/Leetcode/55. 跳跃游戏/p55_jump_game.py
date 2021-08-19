from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        if n < 2:
            return True
        hole = [i for i in range(n-1) if nums[i] == 0]
        t = 0
        res = []
        if hole:
            for h in hole:
                for i in range(t, h):
                    if nums[i] > h-i:
                        t = i
                        res.append(1)
                        break
                else:
                    res.append(0)
        return all(res)


s = Solution()
a = [3, 2, 1, 0, 4]
res = s.canJump(a)
print(res)
