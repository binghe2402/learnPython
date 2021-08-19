class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        mat = [[0]*(n+1) for i in range(m+1)]
        mat[1][1] = 1
        for i in range(1, m+1):
            for j in range(1, n+1):
                if 0 < i <= m and 0 < j <= n and not mat[i][j]:
                    mat[i][j] = mat[i-1][j]+mat[i][j-1]

        return mat[m][n]


s = Solution()
print(s.uniquePaths(3, 7))
