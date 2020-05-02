from numpy.random import randint


def shells_sort(nums):
    gap = len(nums)//2
    while gap > 0:
        for i in range(gap):
            for j in range(i+gap, len(nums), gap):
                k = nums[j]
                while j > i and k < nums[j-gap]:
                    nums[j] = nums[j-gap]
                    j -= gap
                else:
                    nums[j] = k
        gap //= 2
    return nums


nums = list(randint(1, 100, 1000))
res = shells_sort(nums)
print(res)
print(sorted(nums) == res)
