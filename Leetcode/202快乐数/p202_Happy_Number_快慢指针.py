class Solution:
    def isHappy(self, n: int) -> bool:
        def getHappy(n):
            res = 0
            while n:
                n, m = divmod(n, 10)
                res += m**2
            return res
        fast, slow = getHappy(n), n
        while fast != slow and fast > 1:
            fast = getHappy(getHappy(fast))
            slow = getHappy(slow)
        else:
            return fast == 1
