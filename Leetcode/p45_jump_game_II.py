from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        step = 1
        cur = 0
        while cur + nums[cur] < len(nums)-1:
            max_dist = 0
            for i in range(1, nums[cur]+1):
                if cur+i < len(nums) and nums[cur+i]+i > max_dist:
                    max_dist = nums[cur + i] + i
                    max_i = i
            cur += max_i
            step += 1

        return step


nums = [2, 3, 1]
s = Solution()
res = s.jump(nums)
print(res)
