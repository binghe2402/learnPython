
class Solution:
    def twoSum(self, nums, target):
        hashmap = {}
        for i, num in enumerate(nums):
            if (target - num) in hashmap:
                return [i, hashmap[target - num]]
            hashmap[num] = i


s = Solution()
nums = [2, 2]
target = 4
print(s.twoSum(nums, target))
