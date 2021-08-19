# HT13198 庄淼


def checkRaise(n: int, an: list):
    # if n == 1:
    #     return 'yes'
    an.append(float('inf'))
    an.append(float('-inf'))
    i = 0
    while i < n and an[i] > an[i-1]:
        i += 1
    if not i < n:
        return 'yes'
    l = an[i-1]
    ll = an[i-2]
    while i < n and an[i] < an[i-1]:
        i += 1

    if an[i-1] < ll or l > an[i]:
        return 'no'
    if not i < n:
        return 'yes'
    while i < n and an[i] > an[i-1]:
        i += 1
    if not i < n:
        return 'yes'
    else:
        return 'no'


t = int(input())
res = []

for i in range(t):
    n = int(input())
    an = [int(x) for x in input().split()]
    res.append(checkRaise(n, an))

for r in res:
    print(r)
