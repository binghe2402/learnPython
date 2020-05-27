from typing import List
import collections
'''
前缀和
n*K = sum[i+1:j+1] = prefixSum[j]-prefixSum[i]
(prefixSum[i] - prefixSum[j]) % K == 0
prefixSum[i] % K ==  prefixSum[j] % K


'''


class Solution:
    def subarraysDivByK(self, A: List[int], K: int) -> int:
        prefixSum = 0
        prefix_cnt = collections.Counter({0: 1})
        cnt = 0
        for i in A:
            prefixSum += i
            prefixSum_mod = prefixSum % K
            cnt += prefix_cnt[prefixSum_mod]
            prefix_cnt[prefixSum_mod] += 1
        return cnt


A = [4, 5, 0, -2, -3, 1]
K = 5
s = Solution()
res = s.subarraysDivByK(A, K)
print(res)
