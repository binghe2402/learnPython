from functools import lru_cache


class Solution:
    def superEggDrop(self, K: int, N: int) -> int:

        @lru_cache(None)
        def f(k, n):
            if n <= 1:
                return 1
            elif k == 1:
                return n
            else:
                left, right = 1, n
                while left+1 < right:
                    mid = (left+right)//2
                    # c = check(mid)
                    f1 = f(k-1, mid-1)
                    f2 = f(k, n-mid)

                    if f1 < f2:
                        left = mid
                    elif f1 > f2:
                        right = mid
                    else:
                        left = right = mid
                return min([max(f(k-1, x-1), f(k, n-x)) for x in [left, right]])+1

        return f(K, N)


s = Solution()
K = 4
N = 5000
res = s.superEggDrop(K, N)
print(res)
