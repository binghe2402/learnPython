from typing import List


class Solution:
    def updateMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        m, n = len(matrix), len(matrix[0])

        dist = [[None]*n for x in range(m)]
        one_set = set()

        for i in range(m):
            for j in range(n):
                # 利用短路特性和返回实际值，当matrix值为1时，设置dist为None，并记录坐标
                dist[i][j] = matrix[i][j] and one_set.add((i, j))

        def check(i, j):
            # direction = ((-1, 0), (1, 0), (0, 1)(0, 1))
            d = [dist[dcti][dctj]
                 for dcti, dctj in ((i-1, j), (i+1, j), (i, j-1), (i, j+1))
                 if 0 <= dcti < m and 0 <= dctj < n
                 if dist[dcti][dctj] is not None
                 if dist[dcti][dctj] <= k]
            if d:
                dist[i][j] = min(d)+1

            if dist[i][j]:
                one_set_remove.add((i, j))
            # i += dcti
            # j += dctj
            # if 0 <= dcti < m and 0 <= dctj < n:
            #         dist[i][j] = min()
        k = 0
        while one_set:
            k += 1
            one_set_remove = set()
            for i, j in one_set:
                check(i, j)
            one_set -= one_set_remove

        return dist


s = Solution()
mat = [[1, 1, 0, 1, 1, 1, 1, 1, 1, 1],
       [1, 1, 0, 1, 1, 1, 1, 1, 1, 1],
       [1, 1, 1, 1, 0, 0, 0, 1, 1, 0],
       [1, 1, 1, 1, 1, 1, 0, 0, 1, 0],
       [1, 0, 0, 1, 1, 1, 0, 1, 0, 1],
       [0, 0, 1, 0, 0, 1, 1, 0, 0, 1],
       [0, 1, 0, 1, 1, 1, 1, 1, 1, 1],
       [1, 0, 0, 1, 1, 0, 0, 0, 0, 0],
       [0, 0, 1, 1, 1, 1, 0, 1, 1, 1],
       [1, 1, 0, 0, 1, 0, 1, 0, 1, 1]]
res = s.updateMatrix(mat)
print(res)
