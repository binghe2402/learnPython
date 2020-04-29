from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) < 3:
            return nums.index(target) if target in nums else -1
        if nums[0] > nums[-1]:
            left, right = 0, len(nums)-1
            while left+1 < right:
                mid = (left+right)//2
                if nums[left] < nums[mid] > nums[right]:
                    left = mid
                else:
                    right = mid

        # 下面二分的写法和区间设置参考
        # 二分查找有几种写法？它们的区别是什么？ - Jason Li的回答 - 知乎
        # https://www.zhihu.com/question/36132386/answer/530313852
            if nums[right] <= target <= nums[-1]:
                left, right = right, len(nums)
            elif nums[left] >= target >= nums[0]:
                left, right = 0, left+1
            else:
                left = right = len(nums)
        else:
            right = len(nums)
            left = 0 if nums[0] <= target else right

        while left < right:
            mid = left + (right-left)//2
            if nums[mid] < target:
                left = mid+1
            elif nums[mid] > target:
                right = mid
            else:
                return mid
        else:
            return -1


s = Solution()
nums = [1, 3, 5]

target = 2
res = s.search(nums, target)
print(res)
