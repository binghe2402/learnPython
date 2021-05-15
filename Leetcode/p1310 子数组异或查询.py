from typing import List


class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        xorL = [0]
        for x in arr:
            xorL.append(xorL[-1] ^ x)

        res = []

        for left, right in queries:
            res.append(xorL[right+1] ^ xorL[left])
        return res
