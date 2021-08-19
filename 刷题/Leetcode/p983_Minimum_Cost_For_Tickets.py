from typing import List


class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        dp = [0]*(days[-1]+1)
        for i in range(1, days[-1]+1):
            dp[i] = min((dp[i-1] if i >= 1 else dp[0]) + costs[0],
                        (dp[i-7] if i >= 7 else dp[0]) + costs[1],
                        (dp[i-30] if i >= 30 else dp[0]) + costs[2]) if i in days else dp[i-1]
        return dp[i]


days = [1, 4, 6, 7, 8, 20]
costs = [7, 2, 15]
s = Solution()
res = s.mincostTickets(days, costs)
print(res)
