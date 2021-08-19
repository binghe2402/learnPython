from typing import List


class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        def search(i, j):
            ext_len = 1
            while i+ext_len < len(matrix) \
                    and j+ext_len < len(matrix[0]) \
                    and matrix[i+ext_len][j+ext_len] == '1' \
                    and all([matrix[i+ext_len][j+s] == '1'
                             and matrix[i+s][j+ext_len] == '1'
                             for s in range(ext_len)]):
                ext_len += 1
            return ext_len
        max_side = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == '1':
                    max_side = max(search(i, j), max_side)

        return max_side**2


mat = [["1", "0", "1", "1", "0"],
       ["1", "1", "0", "1", "1"],
       ["1", "1", "1", "0", "1"],
       ["0", "1", "1", "1", "0"]]
s = Solution()
res = s.maximalSquare(mat)
print(res)
