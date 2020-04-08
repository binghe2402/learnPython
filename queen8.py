# coding=utf-8
''' 八皇后'''


def queen(pool, cur=0):
    '''八皇后'''
    if cur == len(pool):
        print(pool)
        return 0
    for col in range(len(pool)):
        pool[cur], flag = col, True
        for row in range(cur):
            if pool[row] == col or abs(col - pool[row]) == cur - row:
                flag = False
                break
        if flag:
            queen(pool, cur+1)


queen([None]*8)
