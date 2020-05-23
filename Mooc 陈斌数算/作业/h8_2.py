'''列表出现最频繁的元素'''
from collections import Counter


def topKFrequent(nums, k):
    nums = Counter(nums)
    nums = sorted(nums.items(), key=lambda x: (x[1], -x[0]), reverse=1)[:k]
    return [num[0] for num in nums]


lst = eval(input())
k = int(input())
res = topKFrequent(lst, k)

print(('%s '*len(res)).strip() % tuple(i for i in res))
