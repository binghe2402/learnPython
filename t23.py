class Solution:
    def numberOfSteps(self, num: int) -> int:
        num = bin(num)[2:]
        cnt = 2*len(num)-1
        cnt -= num.count('0')
        return cnt


s = Solution()
a = s.numberOfSteps(14)
print(a)
