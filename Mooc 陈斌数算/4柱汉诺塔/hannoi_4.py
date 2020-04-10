def hannoi_4_num_move(n, p, h):
    rest = [0, 1, 3]

    # if not h:
    #
    if n > 2:
        return min(minhannoi4(n, p, h))
    else:
        return rest[n]


def minhannoi4(n, p, h):
    for x in range(1, n+1):
        if h[n-x]:
            yield 2*h[n-x]+p[x]
        else:
            h[n-x] = hannoi_4_num_move(n-x, p, h)
            yield 2*hannoi_4_num_move(n-x, p, h)+p[x]


n = int(input())
p = [2**x-1 for x in range(n+1)]
h = [0 for i in range(n+1)]
nn = hannoi_4_num_move(n, p, h)
print(nn)
