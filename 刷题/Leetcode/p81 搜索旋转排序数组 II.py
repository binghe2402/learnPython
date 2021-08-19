from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        if len(nums) == 0:
            return False
        if len(nums) == 1:
            return nums[0] == target
        # i = 0
        # while i <= (len(nums)//2) and nums[i] == nums[0] == nums[len(nums)-1-i]:
        #     i += 1
        # if i > len(nums)//2:
        #     return nums[0] == target
        # left, right = i, len(nums)-i-1
        left, right = 0, len(nums)-1
        while left < right:
            mid = left+(right-left)//2
            if nums[mid] == target:
                return True

            if nums[mid] == nums[left] and nums[mid] == nums[right]:
                left += 1
                right -= 1
            elif nums[left] <= nums[mid]:
                if nums[left] <= target < nums[mid]:
                    right = mid
                else:
                    left = mid+1
            else:
                if nums[mid] < target <= nums[right]:
                    left = mid+1
                else:
                    right = mid

        return nums[left] == target


nums = [1, 3]
target = 0
s = Solution()
res = s.search(nums, target)
print(res)
