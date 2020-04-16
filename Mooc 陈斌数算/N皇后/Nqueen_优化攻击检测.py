class Solution:
    def totalNQueens(self, n: int) -> int:
        board = [[0]*n for i in range(n)]
        list_b1 = set()
        list_b2 = set()
        list_j = set()

        def check(i, j):
            return not (j in list_j
                        or (i+j) in list_b1
                        or (i-j) in list_b2)

        def forbid_mem(i, j, flag):
            if flag:
                list_b1.add(i+j)
                list_b2.add(i-j)
                list_j.add(j)
            else:
                list_b1.remove(i+j)
                list_b2.remove(i-j)
                list_j.remove(j)

        res = [0]

        def backtrack(i):
            if i == n:
                res[0] += 1
                return
            for j in range(n):
                if check(i, j):
                    board[i][j] = 1
                    forbid_mem(i, j, 1)
                    backtrack(i+1)
                    forbid_mem(i, j, 0)
                    board[i][j] = 0

        backtrack(0)
        return res[0]


s = Solution()
N = 8
res = s.totalNQueens(N)
print(res)
