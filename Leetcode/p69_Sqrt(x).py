class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2:
            return x
        left, right = 0, x
        while left < right:
            # 注意：这里一定取右中位数，如果取左中位数，代码可能会进入死循环
            # mid = left + (right - left + 1) // 2
            mid = (left + right + 1) >> 1
            square = mid * mid

            if square > x:
                right = mid - 1
            else:
                left = mid
        # 因为一定存在，因此无需后处理
        return left
    '''
        def mySqrt(self, x: int) -> int:
        if x < 2:
            return x
        left, right = 0, x
        while left+1 < right:
            mid = left+(right-left)//2
            sq = mid**2
            if sq == x:
                return mid
            elif sq > x:
                right = mid
            else:
                left = mid
        return left
    '''
    '''
    def mySqrt(self, x: int) -> int:
        l, r, ans = 0, x, -1
        while l <= r:
            mid = (l + r) // 2
            if mid * mid <= x:
                ans = mid
                l = mid + 1
            else:
                r = mid - 1
        return ans
    '''


X = list(range(2, 1000))
s = Solution()
res = [s.mySqrt(x) for x in X]
print(res)
root = [int(x**0.5) for x in X]
print(root == res)
