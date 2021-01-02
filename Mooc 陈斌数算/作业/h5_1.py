def Num_base_M_to_N(num_str, M, N):

    base = '0123456789' + ''.join(chr(x) for x in range(ord('A'), ord('Z')+1))

    def trans_M_to_10(num_str, M):
        # d = base[num[-1]]
        return base.index(num_str[-1])+M*trans_M_to_10(num_str[:-1], M) if len(num_str[:-1]) else base.index(num_str[-1])

    def trans_10_to_N(num, N):
        num, m = divmod(num, N)
        if num:
            return trans_10_to_N(num, N) + base[m]
        else:
            return base[m]
    return trans_10_to_N(trans_M_to_10(num_str, M), N)


M, N = map(int, input().split())
num_str = input()
n = Num_base_M_to_N(num_str, M, N)
print(n)
