def maxIntrest(seq):
    if len(seq) < 2:
        return max(seq)
    dp = [None]*len(seq)                   # 前i间的最大
    dp[0], dp[1] = seq[0], max(seq[:2])
    for i in range(2, len(seq)):
        dp[i] = max(dp[i-2]+seq[i], dp[i-1])
    return dp[-1]


if __name__ == "__main__":
    seq = list(map(int, input().split()))
    res = maxIntrest(seq)
    print(res)
