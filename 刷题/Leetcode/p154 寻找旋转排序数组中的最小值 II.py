from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        left, right = 0, len(nums)-1
        while left < right and nums[left] >= nums[0]:
            mid = left + (right-left)//2
            if nums[mid] == nums[left] == nums[right]:
                left += 1
                right -= 1
            elif nums[mid] >= nums[left]:
                left = mid+1
            else:
                right = mid

        return min(nums[left], nums[0])
