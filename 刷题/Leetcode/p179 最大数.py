from typing import List
import functools


class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        nums = [str(x) for x in nums]
        # 它有两个传入参数x,y 当x>y时返回1 等于时返回0，否则返回-1。
        # 它在list中的工作机制就是将列表中的元素去两两比较，当cmp返回是正数时 交换两元素”

        def compare(x, y):
            return 1 if x+y < y+x else -1

        nums.sort(key=functools.cmp_to_key(compare))
        res = ''.join(nums)
        return '0'if res[0] == '0' else res
