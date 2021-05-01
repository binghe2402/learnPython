class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        for x in range(int(c**0.5)+1):
            y = (c-x**2)**0.5
            if y == int(y):
                return True
        return False
