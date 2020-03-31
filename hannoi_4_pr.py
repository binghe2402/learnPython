def hannoi_4_num_move(n, h):
    h[0:3] = [0, 1, 3]
    if h[n] is not None:
        return h[n]
    elif n > 2:
        h[n] = min([2*hannoi_4_num_move(n-x, h)+2**x-1 for x in range(1,n+1)])
        return h[n]


n = int(input())
p = [2**x-1 for x in range(n+1)]
h = [None]*(n+1)
nn = hannoi_4_num_move(n,h)
print(nn)
