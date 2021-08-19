from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i, j = 0, len(nums)-1
        while i <= j:
            while i < len(nums) and nums[i] != val:
                i += 1
            while j >= 0 and nums[j] == val:
                j -= 1
            if i < j:
                nums[i] = nums[j]
                i += 1
                j -= 1
        return j+1


s = Solution()
nums = [1]
val = 1
res = s.removeElement(nums, val)
print(res)
