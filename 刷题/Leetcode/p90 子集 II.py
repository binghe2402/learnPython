from typing import List


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = set()
        path = []
        nums.sort()

        def backtrack(nums):
            res.add(tuple(path[:]))
            for i in range(len(nums)):
                path.append(nums[i])
                backtrack(nums[i+1:])
                path.pop()
        backtrack(nums)
        return [list(x) for x in res]


nums = [1, 2, 2]
s = Solution()
res = s.subsetsWithDup(nums)
print(res)
