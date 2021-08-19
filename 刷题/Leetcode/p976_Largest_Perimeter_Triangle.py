from typing import List


class Solution:
    def largestPerimeter(self, A: List[int]) -> int:
        A.sort(reverse=1)
        i, c = 0, 0
        for i in range(len(A)-2):
            if A[0+i] < A[1+i]+A[2+i]:
                c = sum(A[0+i:3+i])
                break
        return c
