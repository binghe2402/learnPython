from typing import List


class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        Widths = {}
        for row in wall:
            if len(row) == 1:
                continue
            width = 0
            for brick in row[:-1]:
                width += brick
                if width in Widths:
                    Widths[width] += 1
                else:
                    Widths[width] = 1
        return len(wall)-max(Widths.values()) if Widths else len(wall)


s = Solution()
wall = [[1, 2, 2, 1], [3, 1, 2], [1, 3, 2], [2, 4], [3, 1, 2], [1, 3, 1, 1]]
res = s.leastBricks(wall)
print(res)
