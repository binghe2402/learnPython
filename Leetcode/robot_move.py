'''
面试题13. 机器人的运动范围
https://leetcode-cn.com/problems/ji-qi-ren-de-yun-dong-fan-wei-lcof/
'''


class Solution:

    def movingCount(self, m: int, n: int, k: int) -> int:
        self.m = m
        self.n = n
        self.k = k
        self.direction = [(0, 1), (1, 0)]
        self.searched = []

        cnt = self.search(0, 0)
        return cnt

    def search(self, i, j):
        if not(0 <= i < self.m and 0 <= j < self.n):
            return 0
        if sum([int(x) for x in (str(i) + str(j)) if x.isdecimal()]) > self.k:
            return 0
        if (i, j) in self.searched:
            return 0
        self.searched.append((i, j))
        cnt = 1
        for d in self.direction:
            cnt += self.search(i + d[0], j + d[1])
        return cnt


s = Solution()
m = 3
n = 2
k = 17
print(s.movingCount(m, n, k))
