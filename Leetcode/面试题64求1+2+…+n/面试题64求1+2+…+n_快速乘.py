class Solution:
    def sumNums(self, n: int) -> int:
        # sumN = n*(n+1)//2
        # sumN = n*(n+1) >>1
        # 将n+1展开为2**i的级数，这也就是展开为其二进制的每一位，这又可转化为位运算 1 & (n+1)>>i
        # 由于已知1 <= n <= 10000，那么写出全部的15位即可
        # sumN = n*(∑2**i)>>1
        # sumN = ∑((1 & (n+1)>>i) and (n<<i))
        # n0 = ((1 & (n+1) >> 0) and (n << 0))
        # n1 = ((1 & (n+1) >> 1) and (n << 1))
        # n1 = ((1 & (n+1) >> 2) and (n << 2))
        # ...
        # n14 = ...

        opN_1, opN_2 = n, n+1
        sumN = (1 & opN_2) and opN_1
        opN_1 <<= 1
        opN_2 >>= 1
        sumN += (1 & opN_2) and opN_1
        opN_1 <<= 1
        opN_2 >>= 1
        sumN += (1 & opN_2) and opN_1
        opN_1 <<= 1
        opN_2 >>= 1
        sumN += (1 & opN_2) and opN_1
        opN_1 <<= 1
        opN_2 >>= 1
        sumN += (1 & opN_2) and opN_1
        opN_1 <<= 1
        opN_2 >>= 1
        sumN += (1 & opN_2) and opN_1
        opN_1 <<= 1
        opN_2 >>= 1
        sumN += (1 & opN_2) and opN_1
        opN_1 <<= 1
        opN_2 >>= 1
        sumN += (1 & opN_2) and opN_1
        opN_1 <<= 1
        opN_2 >>= 1
        sumN += (1 & opN_2) and opN_1
        opN_1 <<= 1
        opN_2 >>= 1
        sumN += (1 & opN_2) and opN_1
        opN_1 <<= 1
        opN_2 >>= 1
        sumN += (1 & opN_2) and opN_1
        opN_1 <<= 1
        opN_2 >>= 1
        sumN += (1 & opN_2) and opN_1
        opN_1 <<= 1
        opN_2 >>= 1
        sumN += (1 & opN_2) and opN_1
        opN_1 <<= 1
        opN_2 >>= 1
        sumN += (1 & opN_2) and opN_1
        opN_1 <<= 1
        opN_2 >>= 1
        sumN += (1 & opN_2) and opN_1

        return sumN >> 1
