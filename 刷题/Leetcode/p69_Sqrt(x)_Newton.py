class Solution:
    def mySqrt(self, x: int) -> int:
        C = x
        while x**2-C > 1e-6:
            x = (x+C/x)/2
        return int(x)


X = list(range(2, 1000))
s = Solution()
res = [s.mySqrt(x) for x in X]
print(res)
root = [int(x**0.5) for x in X]
print(root == res)
