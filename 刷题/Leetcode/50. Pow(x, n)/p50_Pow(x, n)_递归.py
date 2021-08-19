class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 1:
            return x*x
        n, i = divmod(n, 2)
        y = self.myPow(x, n)
        if i:
            return y*y*x
        else:
            return y*y
