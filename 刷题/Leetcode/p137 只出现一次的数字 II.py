from typing import List
from collections import Counter


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # cnt = {}
        # for i in nums:
        #     if i in cnt:
        #         cnt[i] += 1
        #     else:
        #         cnt[i] = 1
        ####
        # cnt = Counter()
        # for i in nums:
        #     cnt[i] += 1
        ####
        cnt = Counter(nums)

        for i in cnt:
            if cnt[i] == 1:
                return i
