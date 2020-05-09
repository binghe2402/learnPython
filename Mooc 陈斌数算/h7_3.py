import random
# nums = list(map(int, input().split()))
# nums_liter = list(map(int, input().split()))

merge_liter = []
insert_liter = []


def merge_sort(nums):
    def divide(nums):
        if len(nums) == 1:
            return nums
        else:
            mid = len(nums)//2
            nums1 = divide(nums[:mid])
            nums2 = divide(nums[mid:])
            return merge(nums1, nums2)

    def merge(nums1, nums2):
        i = j = 0
        nums = []
        while i < len(nums1) and j < len(nums2):
            if nums1[i] > nums2[j]:
                nums.append(nums2[j])
                j += 1
            else:
                nums.append(nums1[i])
                i += 1
        if i < len(nums1):
            nums.extend(nums1[i:])
        else:
            nums.extend(nums2[j:])
        # merge_liter.append(nums[:])
        return nums
    return divide(nums)


def insert_sort(nums):
    for i in range(1, len(nums)):
        temp = nums[i]
        for j in range(1, i):
            if temp < nums[i-j]:
                nums[i-j+1] = nums[i-j]
            else:
                nums[i-j+1] = temp
        # yield nums
    return nums


nums = [random.randint(1, 200) for i in range(1000)]
true_sort = sorted(nums)
merge = merge_sort(nums)
insert = insert_sort(nums)
print(merge_liter)
print(insert)
print("merge_sort:%r" % (merge == true_sort))
print("insert_sort:%r" % (insert[-1] == true_sort))
