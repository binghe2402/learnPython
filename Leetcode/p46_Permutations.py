from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        select_nums = set(nums)
        ans = []

        def backtrack(nums):
            if len(select_nums) == 1:
                res.extend(select_nums)
                ans.append(res[:])
                res.pop()
            else:
                for i in nums:
                    if i in select_nums:
                        res.append(i)
                        select_nums.remove(i)
                        backtrack(nums)
                        select_nums.add(i)
                        res.pop()
        backtrack(nums)
        return ans


nums = [1, 2, 3]
s = Solution()
res = s.permute(nums)
print(res)
