class Num_base_M_to_N:
    base = ''.join([chr(x) for x in range(ord('0'), ord('9')+1)] +
                   [chr(x) for x in range(ord('A'), ord('Z')+1)])

    def num_base_MtoN(self, num: str, M, N) -> str:
        num = self.Mnum_baseMto10(num, M)//M
        return self.num_base_10toN(num, N)

    def Mnum_baseMto10(self, num: str, M) -> int:
        digt = self.base.index(num[-1])
        num = num[:-1]
        if len(num) > 0:
            return (digt + self.Mnum_baseMto10(num, M))*M
        else:
            return digt*M

    def num_base_10toN(self, num: int, N) -> str:
        num, digt = divmod(num, N)
        if num > 0:
            return self.num_base_10toN(num, N)+self.base[digt]
        else:
            return self.base[digt]


c = Num_base_M_to_N()
M, N = map(int, input().split())
num = input()
n = c.num_base_MtoN(num, M, N)
print(n)
# print("%x" % num)
