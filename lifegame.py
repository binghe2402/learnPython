from typing import List


class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        m = len(board)
        n = len(board[0])
        new_board = [l[:] for l in board]

        def numOflive():
            cnt = 0
            for a in (i-1, i, i+1):
                for b in (j-1, j, j+1):
                    if (0 <= a < m) and \
                        (0 <= b < n) and \
                            (not (a == i and b == j)):
                        cnt += new_board[a][b]
            return cnt

        for i in range(m):
            for j in range(n):
                num = numOflive()
                if num < 2:
                    board[i][j] = 0
                elif num == 3:
                    board[i][j] = 1
                elif num > 3:
                    board[i][j] = 0
                else:
                    board[i][j] = new_board[i][j]
        a = 1

        # board[i][j] = [0, 0, 1, 1, 0, 0, 0, 0]

        """
        Do not return anything, modify board in-place instead.
        """


board = [[0, 1, 0],
         [0, 0, 1],
         [1, 1, 1],
         [0, 0, 0]]
s = Solution()
s.gameOfLife(board)
