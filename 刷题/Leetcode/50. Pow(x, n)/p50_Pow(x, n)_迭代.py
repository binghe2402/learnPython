class Solution:
    def myPow(self, x: float, n: int) -> float:
        res = 1
        postive = n > 0
        n = abs(n)
        while n:
            n, i = divmod(n, 2)
            res = res*x if i else res
            x *= x
        return res if postive else 1/res
