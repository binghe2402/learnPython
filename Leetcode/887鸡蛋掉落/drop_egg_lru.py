from functools import lru_cache


class Solution:
    def superEggDrop(self, K: int, N: int) -> int:
        @lru_cache(None)
        def F(k, n):
            if k == 1:
                return n
            if n <= 1:
                return 1
            x = 1
            f = F(k, n-(x))+1

            for x in range(2, n):
                temp = max(F(k, n-(x))+1, F(k-1, x-1)+1)
                if temp < f:
                    f = temp

            x = n
            temp = F(k-1, x-1)+1
            if temp < f:
                f = temp
            return f

        for k in range(1, K+1):
            for n in range(1, N+1):
                f = F(k, n)

        return f


s = Solution()
K = 4
N = 5000
res = s.superEggDrop(K, N)
print(res)
