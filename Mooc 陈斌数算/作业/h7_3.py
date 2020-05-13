# import random
nums = list(map(int, input().split()))
nums_liter = list(map(int, input().split()))

merge_liter = []
insert_liter = []


def merge_sort(nums):
    nums = nums[:]

    def merge(nums1, nums2):
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
        yield nums
    # return nums


def insert_sort(nums):
    nums = nums[:]
    for i in range(1, len(nums)):
        temp = nums[i]
        j = 1
        # for j in range(1, i+1):
        while j <= i and temp < nums[i-j]:
            # if temp < nums[i-j]:
            nums[i-j+1] = nums[i-j]
            j += 1
        else:
            nums[i-j+1] = temp
            # break
        yield nums
    # return nums


# nums = [random.randint(1, 200) for i in range(1000)]
true_sort = sorted(nums)
merge_liter = merge_sort(nums)
insert_liter = insert_sort(nums)
for seq in merge_liter:
    if seq == nums_liter:
        print('Merge Sort')
        print(('%d '*len(nums)).strip() % tuple(i for i in next(merge_liter)))
        break

for seq in insert_liter:
    if seq == nums_liter:
        print('Insertion Sort')
        print(('%d '*len(nums)).strip() % tuple(i for i in next(insert_liter)))
        break
