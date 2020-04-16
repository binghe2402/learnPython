from typing import List


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board = [['.']*n for i in range(n)]

        def check(i, j):
            for k in range(n):
                if board[i][k] == 'Q':
                    break
                if board[k][j] == 'Q':
                    break
                b1 = i+j
                b2 = i-j
                if 0 <= k < n and 0 <= b1-k < n and board[k][b1-k] == 'Q':
                    break
                if 0 <= k < n and 0 <= -b2+k < n and board[k][k-b2] == 'Q':
                    break
            else:
                return True
            return False

        res_r = []
        res = []

        def find(i):
            if i == n:
                res.append(res_r[:])
                return
            for j in range(n):
                if check(i, j):
                    board[i][j] = 'Q'
                    res_r.append(''.join(board[i]))
                    find(i+1)
                    board[i][j] = '.'
                    res_r.pop()
        find(0)

        return res


s = Solution()
N = 4
res = s.solveNQueens(N)


for sol in res:
    for row in sol:
        for c in row:
            print(c, end=' ')
        print()
    print()
