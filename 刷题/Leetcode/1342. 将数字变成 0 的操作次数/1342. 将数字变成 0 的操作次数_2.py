class Solution:
    def numberOfSteps(self, num: int) -> int:
        num = bin(num)[2:]
        cnt = -1
        for i in num:
            if i == '1':
                cnt += 2
            else:
                cnt += 1
        return cnt
