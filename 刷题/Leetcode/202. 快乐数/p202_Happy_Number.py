class Solution:
    def isHappy(self, n: int) -> bool:
        def getHappy(n):
            res = 0
            while n:
                n, m = divmod(n, 10)
                res += m**2
            return res
        lst = set()
        while n not in lst:
            if n == 1:
                return True
            lst.add(n)
            n = getHappy(n)
        else:
            return False
