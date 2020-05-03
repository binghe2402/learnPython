from numpy.random import randint
from typing import List


def quick_sort(nums: List):
    def sort(left, right):
        i, j = left, right
        if left < right:
            mid_val = nums[left]
            while i < j:
                while i < j and nums[j] >= mid_val:
                    j -= 1
                while i < j and nums[i] <= mid_val:
                    i += 1
                if i < j:
                    nums[i], nums[j] = nums[j], nums[i]
            nums[left], nums[i] = nums[i], nums[left]
            sort(left, i-1)
            sort(i+1, right)
    sort(0, len(nums)-1)
    return nums


nums = list(randint(1, 100, 500))
res = quick_sort(nums)
print(res)
print(sorted(nums) == res)
