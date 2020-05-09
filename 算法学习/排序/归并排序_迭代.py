
from typing import List
from numpy.random import randint
import multiprocessing as mp


def merge_sort(nums: List):
    nums = nums[:]

    def merge(nums1: List, nums2: List):
        nums = []
        i = j = 0
        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                nums.append(nums1[i])
                i += 1
            else:
                nums.append(nums2[j])
                j += 1
        if i < len(nums1):
            nums.extend(nums1[i:])
        elif j < len(nums2):
            nums.extend(nums2[j:])
        return nums

    gap = 1
    while gap <= len(nums):
        gap *= 2
        for i in range(0, len(nums), gap):
            nums_cell = nums[i:i+gap]
            mid = gap//2
            nums1 = nums_cell[:mid]
            nums2 = nums_cell[mid:]
            if nums2:
                nums[i:i+gap] = merge(nums1, nums2)

    return nums


nums = [list(randint(1, 900, i)) for i in range(2000)]
res = all([merge_sort(i) == sorted(i) for i in nums])
print(res)
# print(sorted(nums) == res)
