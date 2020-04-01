def hannoi_4_num_move(n, h):
    if n < 3:
        h[0:3] = [0, 1, 3]
    if h[n] is not None:
        return h[n]
    elif n > 2:
        # x不可能取到n，否则就是把这一堆整体移动，没有意义
        h[n] = min([2*hannoi_4_num_move(n-x, h)+2**x-1 for x in range(1, n)])
        return h[n]


# n = int(input())
n = 10
p = [2**x-1 for x in range(n+1)]
h = [None]*(n+1)
nn = hannoi_4_num_move(n, h)
print(nn)
