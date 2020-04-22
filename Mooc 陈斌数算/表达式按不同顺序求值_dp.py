import re
s = input()
s = re.split(r'([\+\-\*])', s)
num = []
op = []
for ch in s:
    if ch.isdecimal():
        num.append(ch)
    else:
        op.append(ch)


def rest(a, b):
    r = '('
    for i in range(a, b):
        r += (num[i]+op[i])
    r += (num[b]+')')
    return r


n = len(num)

dp = [[] for i in range(n+1)]
dp[1].append(num[0])
for i in range(1, len(num)):
    if not dp[i]:
        for j in range(1, i):
            dp[i].extend([c+op[i-j-1]+rest(i-j, j) for c in dp[i-j]])


print(dp[-1])
