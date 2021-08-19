from typing import List


class Solution:
    def surfaceArea(self, grid: List[List[int]]) -> int:
        # 顶面和底面面积容易确定
        cnt = 0
        area = 0
        self.m = len(grid)
        self.n = len(grid[0])
        self.grid = grid

        for y in range(self.m):
            for x in range(self.n):
                if self.grid[y][x]:
                    slide = self.__slide_area(x, y)
                    area += slide
                    cnt += 1

        for y in range(self.m):
            for x in range(self.n):
                if self.grid[y][x]:
                    self.grid[y][x] -= 1
                    if self.grid[y][x]:
                        flag = 1
        area += cnt*2
        return area

    def __slide_area(self, x, y):
        slide = 0
        if x + 1 < self.n:
            slide += max(self.grid[y][x] - self.grid[y][x+1], 0)
        else:
            slide += self.grid[y][x]

        if x - 1 >= 0:
            slide += max(self.grid[y][x] - self.grid[y][x-1], 0)
        else:
            slide += self.grid[y][x]
        if y + 1 < self.m:
            slide += max(self.grid[y][x] - self.grid[y+1][x], 0)
        else:
            slide += self.grid[y][x]
        if y - 1 >= 0:
            slide += max(self.grid[y][x] - self.grid[y-1][x], 0)
        else:
            slide += self.grid[y][x]
        return slide


grd = [[1, 0], [0, 2]]
s = Solution()
area = s.surfaceArea(grd)
print(area)
