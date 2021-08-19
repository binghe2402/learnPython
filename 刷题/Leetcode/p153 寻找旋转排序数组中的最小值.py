from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums)
        while left < right and nums[left] >= nums[0]:
            mid = left+(right-left)//2
            if nums[mid] < nums[left]:
                right = mid
            else:
                left = mid+1
        return nums[left] if left < len(nums) else nums[0]
