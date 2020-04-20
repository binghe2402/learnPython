from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        cnt = 0

        def check(i, j):
            return 0 <= i < len(grid) \
                and 0 <= j < len(grid[0]) \
                and grid[i][j] == '1'

        def search(i, j):
            for di, dj in ((i-1, j+0), (i+1, j+0), (i+0, j-1), (i+0, j+1)):
                if check(di, dj):
                    neighbors.append((di, dj))
                    grid[di][dj] = 0
                while neighbors:
                    for di, dj in neighbors:
                        neighbors.remove((di, dj))
                        search(di, dj)

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if check(i, j):
                    neighbors = []
                    grid[i][j] = 0
                    search(i, j)
                    cnt += 1
        return cnt


s = Solution()
grid = [["1", "1", "0", "0", "0"],
        ["1", "1", "0", "1", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "0", "1", "0"]]
res = s.numIslands(grid)
print(res)
