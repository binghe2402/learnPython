class Solution:
    def clumsy(self, N: int) -> int:
        stackN = [N]
        stackop = [1]
        N -= 1
        for i in range(1, N):
            if i % 4 == 1:
                stackN[-1] *= N
