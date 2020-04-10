'''
lru_cache装饰器的运行效率比自己动手做备忘录更高
但是定义装饰器会产生较高的时间开销
如果把函数定义部分放进计时，那么lru_cache版本的就会比手动慢10倍
但如果挪出来，lrc版只需要手动版1/3的时间
'''

import timeit

ss = \
    '''
n = 10
h = [None]*(n+1)
from functools import lru_cache

@lru_cache(None)
def hannoi_4_num_move_lru(n):
    if n < 3:
        return [0, 1, 3][n]
    else:
        # x不可能取到n，否则就是把这一堆整体移动，没有意义
        return min([2*hannoi_4_num_move_lru(n-x)+2**x-1 for x in range(1, n)])

def hannoi_4_num_move(n, h):
    if n < 3:
        h[0:3] = [0, 1, 3]
    if h[n] is not None:
        return h[n]
    elif n > 2:
        # x不可能取到n，否则就是把这一堆整体移动，没有意义
        h[n] = min([2*hannoi_4_num_move(n-x, h)+2**x-1 for x in range(1, n)])
        return h[n]
'''


s1 = \
    '''
nn = hannoi_4_num_move_lru(n)
'''


s2 = \
    '''
nn = hannoi_4_num_move(n, h)
'''

t1 = timeit.timeit(stmt=s1, setup=ss, number=2000000)
t2 = timeit.timeit(stmt=s2, setup=ss, number=2000000)
print(t1)
print(t2)
