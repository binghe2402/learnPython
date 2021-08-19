from typing import List
'''
dp[i][j]为最大的右下角为i,j的正方形的边长
dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])+1
dp[i-1][j] 上方格子， 确定竖直边的边长
dp[i][j-1] 左方格子， 确定水平边的边长
dp[i-1][j-1] 左上格子，确定对角线长。

可以直接matrix矩阵本身来记录作为dp，降低空间复杂度
'''


class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        max_side = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                matrix[i][j] = int(matrix[i][j])
                if matrix[i][j]:
                    if i == 0 or j == 0:
                        matrix[i][j] = 1
                    else:
                        matrix[i][j] = min(matrix[i-1][j],
                                           matrix[i][j-1],
                                           matrix[i-1][j-1])+1
                    max_side = max(max_side, matrix[i][j])
        return max_side**2


mat = [["1", "0", "1", "1", "0"],
       ["1", "1", "0", "1", "1"],
       ["1", "1", "1", "0", "1"],
       ["0", "1", "1", "1", "0"]]
s = Solution()
res = s.maximalSquare(mat)
print(res)
