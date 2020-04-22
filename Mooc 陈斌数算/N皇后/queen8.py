# coding=utf-8
''' 
八皇后
pool列表，index表示行，值表示列，如pool[1]=2，则表示放在(1,2)处
为什么不需要显式的回溯法？
本身这样储存棋子位置，在每行只能有一个列位置，
因此设置新值就会自动的撤销旧值，而不需要回溯法显式的改回棋子。
而检测攻击位置，只检测前面的行即可，后面的行当不存在。

'''

aaa = []


def queen(pool, cur=0):
    '''八皇后'''
    if cur == len(pool):
        aaa.append(pool)
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
print(len(aaa))
