from typing import List


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        L = Lmax = 0
        for i in nums:
            if i:
                L += 1
            else:
                if Lmax < L:
                    Lmax = L
                L = 0
        return max(Lmax, L)
