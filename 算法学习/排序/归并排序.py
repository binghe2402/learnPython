def merge_sort(nums):
    # def divide(nums):
    #     if len(nums) == 1:
    #         return nums, []
    #     else:
    #         return nums[:len(nums)//2], nums[len(nums)//2:]

    def merge(nums1, nums2):
        new_nums = []
        i = j = 0
        while i < len(nums1) or j < len(nums2):
            if j >= len(nums2) or (i < len(nums1) and nums1[i] < nums2[j]):
                new_nums.append(nums1[i])
                i += 1
            else:
                new_nums.append(nums2[j])
                j += 1
        return new_nums

    def sort(nums):
        left, right = 0, len(nums)
        if left+1 < right:
            mid = (left+right)//2
            nums1 = nums[left:mid]
            nums2 = nums[mid:right]
            return merge(sort(nums1), sort(nums2))
        else:
            return nums

    return sort(nums)


a = [1213, 34, 21, 3, 56, 2, 4, 5, 4, 3, 5, 6, 7, 65, 434, 2]
print(merge_sort(a))
