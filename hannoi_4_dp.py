def hannoi_4_num_move(n):
    han4 = [0]*(n+1)
    han4[0:3] = [0, 1, 3]
    han3 = [2**x-1 for x in range(n+1)]
    for i in range(2, n+1):
        for x in range(1, i):
            minhan4 = 2 * han4[i-x] + han3[x]
            if not han4[i] or minhan4 < han4[i]:
                han4[i] = minhan4
    return han4[-1]


n = int(input())
nn = hannoi_4_num_move(n)
print(nn)
