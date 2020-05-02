from typing import List
from numpy.random import randint


def insert_sort(nums: List):
    for i in range(1, len(nums)):
        k = nums[i]
        while i > 0 and k < nums[i-1]:
            nums[i] = nums[i-1]
            i -= 1
        else:
            nums[i] = k
    return nums


nums = list(randint(1, 100, 1000))
res = insert_sort(nums)
print(res)
print(sorted(nums) == res)
