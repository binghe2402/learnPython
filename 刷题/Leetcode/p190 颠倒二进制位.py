class Solution:
    def reverseBits(self, n: int) -> int:
        res = 1
        cnt = 0
        while n:
            res <<= 1
            res += (n & 1)
            n >>= 1
            cnt += 1
        res <<= (32-cnt)
        return res & (2**32-1)


s = Solution()
a = 0b00000010100101000001111010011100
res = s.reverseBits(a)
print(bin(res))
