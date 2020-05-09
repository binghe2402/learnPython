from typing import List
from numpy.random import randint


def merge_sort(nums: List):
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

    def devide_sort(nums: List):
        if len(nums) == 1:
            return nums
        else:
            mid = len(nums)//2
            nums1 = devide_sort(nums[:mid])
            nums2 = devide_sort(nums[mid:])
            return merge(nums1, nums2)
    return devide_sort(nums)


nums = list(randint(1, 100, 1000))
res = merge_sort(nums)
print(res)
print(sorted(nums) == res)
