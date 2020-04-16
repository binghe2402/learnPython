from functools import lru_cache


class Solution:
    def superEggDrop(self, K: int, N: int) -> int:
        @lru_cache(None)
        def F(k, n):
            if k == 1:
                return n
            if n <= 1:
                return 1
            f = n
            for x in range(1, n+1):
                temp = max(F(k, n-(x)), F(k-1, x-1))+1
                if temp < f:
                    f = temp
            return f

        for k in range(1, K+1):
            for n in range(1, N+1):
                f = F(k, n)

        return f


s = Solution()
K = 4
N = 50
res = s.superEggDrop(K, N)
print(res)
