def solveNQueen(N):
    pool = [None]*8

    def queen(cur=0):
        if cur == len(pool):
            return 0
        res =  # <Y>
        for col in range(len(pool)):
            pool[cur], flag = col, True
            for row in range(cur):
                if pool[row] == col or abs(col - pool[row]) == cur - row:
                    flag = False
                    break
            if flag:
                res += queen(cur+1)
        return res

    return queen(0)


# test
print(solveNQueen(8))
