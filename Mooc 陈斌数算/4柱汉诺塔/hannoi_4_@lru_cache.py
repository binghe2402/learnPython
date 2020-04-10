from functools import lru_cache
@lru_cache(None)
def hannoi_4_num_move(n):
    if n < 3:
        return [0, 1, 3][n]
    else:
        # x不可能取到n，否则就是把这一堆整体移动，没有意义
        h = min([2*hannoi_4_num_move(n-x)+2**x-1 for x in range(1, n)])
        return h


# n = int(input())
n = 10

nn = hannoi_4_num_move(n)
print(nn)
