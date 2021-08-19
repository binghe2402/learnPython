from typing import List


class Solution:
    def matrixReshape(self, nums: List[List[int]], r: int, c: int) -> List[List[int]]:
        if r*c != len(nums)*len(nums[0]):
            return nums
        new_nums = [[None]*c for i in range(r)]
        # nums = [N for N in nums]
        for i in range(r):
            for j in range(c):
                N = i*c+j
                new_nums[i][j] = nums[N//len(nums[0])][N % len(nums[0])]
        return new_nums


nums = [[1, 2, 4, 5], [3, 4, 5, 7]]
r, c = 4, 2
s = Solution()
res = s.matrixReshape(nums, r, c)
print(res)
