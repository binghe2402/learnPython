from collections import Counter


# def Counter(lst):
#     cnt = {}
#     for i in lst:
#         if i in cnt:
#             cnt[i] += 1
#         else:
#             cnt[i] = 1
#     return cnt


def findAnagrams(s, p):
    p = Counter(p)
    res = []
    for i in range(len(s)-len(p)+1):
        if p == Counter(s[i:i+len(p)]):
            res.append(i)
    return res if res else ['none']


s = input()
p = input()
res = findAnagrams(s, p)
print(('%s '*len(res)).strip() % tuple(i for i in res))
