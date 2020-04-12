class Solution:
    def superEggDrop(self, K: int, N: int) -> int:
        F = [[0]*(N) for i in range(K)]
        F[0] = [n for n in range(1, N+1)]
        for i in range(K):
            F[i][0] = 1

        for k in range(1, K):
            for n in range(1, N):
                x = 0
                F[k][n] = F[k][n-(x+1)]+1
                for x in range(1, n):
                    temp = max(F[k][n-(x+1)]+1, F[k-1][x-1]+1)
                    if temp < F[k][n]:
                        F[k][n] = temp
                x = n
                temp = F[k-1][x-1]+1
                if temp < F[k][n]:
                    F[k][n] = temp

                # F[k][n] = min([max(F[k][n-(x-1)], F[k-1][x-1])
                #                for x in range(1, n+1)])

        return F[-1][-1]


# F[2][2]=min([max(F[2][2-(x-1)]),F[1][x-1]) for x in range(1,2)])
s = Solution()
K = 4
N = 5000
res = s.superEggDrop(K, N)
print(res)
