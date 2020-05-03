from numpy.random import randint
from typing import List


def quick_sort(nums: List):
    def sort(left, right):
        i, j = left, right
        if left < right:
            mid_val = nums[left]

            # 先移动 i 还是先移动 j 的问题。
            # 如果最后i j 停止时重合，那就先移动j，如现在的版本。即 i、j每次移动时，停止条件为 i < j
            # 移动基准数（mid_val)时，交换i和基准数。不过由于i j 重合，所以实际交换j也可以。
            # 递归分解时，用i分段。
            #
            # 如果i、j每次移动时，停止条件为 i <= j。那么最后停止时，i在j的右边。
            # 这时就要先移动 i。移动基准数时，必须交换 j 和基准数。
            # 因为要求交换后基准值左侧都比基准值小，而nums[j]才满足这个要求。
            # 后面递归分解，也是用基准值的坐标，也就是 j 来分段。
            # nums[i]\[j]与mid_val的判断中，必须带着等号（其实主要是nums[i])，
            # 否则第一次交换nums[i]时就会是nums[left]
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


0 1
1 2
key = 1

2 > 1
