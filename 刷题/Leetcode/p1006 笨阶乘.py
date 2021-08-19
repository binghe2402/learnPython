class Solution:
    def clumsy(self, N: int) -> int:
        def cellop(N):
            x = 0
            # for i in range(4):
            for op in [lambda x: N, lambda x:x*N, lambda x:x//N, lambda x:x-N]:
                if N == 0:
                    break
                # op = [lambda x: N, lambda x:x*N, lambda x:x//N, lambda x:x-N]
                x = op(x)
                # if i == 0:
                #     x = N
                # elif i == 1:
                #     x *= N
                # elif i == 2:
                #     x //= N
                # elif i == 3:
                #     x -= N
                N -= 1
            return x
        if N < 4:
            return cellop(N)
        else:
            res = cellop(N)+(N-3)*2
            for n in range(N-4, 0, -4):
                res -= cellop(n)
            return res


s = Solution()
N = 5
res = s.clumsy(N)
print(res)
