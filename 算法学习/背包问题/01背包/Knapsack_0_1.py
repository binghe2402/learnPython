'''
大盗潜入博物馆，面前有5件宝物，分别有重量和价值，
大盗的背包仅能负重20公斤，请问如何选择宝物，总价值最高？

item  weight   value
  1     2        3
  2     3        4
  3     4        8
  4     5        8
  5     9        10
'''

'''
# 使用字典储存
def knapsack(W, lst):
    # dp[item,w]
    dp = {}
    for i in range(len(lst)):
        dp[i, 0] = 0
    for w in range(W+1):
        dp[0, w] = 0
    for i in range(1, len(lst)):
        for w in range(1, W+1):
            if lst[i]['w'] > w:
                dp[i, w] = dp[i-1, w]
            else:
                dp[i, w] = max(dp[i-1, w], dp[i-1, w-lst[i]['w']]+lst[i]['v'])

    return dp[i, W]
'''

'''
# 使用数组储存
def knapsack(W, lst):
    # dp[item][w]
    dp = [[0]*(W+1) for i in range(len(lst))]
    for i in range(1, len(lst)):
        for w in range(1, W+1):
            if lst[i]['w'] > w:
                dp[i][w] = dp[i-1][w]
            else:
                dp[i][w] = max(dp[i-1][w], dp[i-1][w-lst[i]['w']]+lst[i]['v'])

    return dp[-1][-1]
'''


def knapsack(W, lst):
    # 使用数组储存的空间优化，实际只需要[j]和[j-1]两行
    # dp[item][w]
    dp = [[0]*(W+1), [0]*(W+1)]
    for i in range(1, len(lst)):
        j = i % 2
        for w in range(1, W+1):
            # 实际上w的范围应该直接可以是 range(lst[i]['w],W+1)，至少对于费用都非负时
            if lst[i]['w'] > w:
                dp[j][w] = dp[j-1][w]
            else:
                dp[j][w] = max(dp[j-1][w], dp[j-1][w-lst[i]['w']]+lst[i]['v'])
            # 或者不else 而是直接
            # dp[j][w] = max(dp[j][w], dp[j-1][w-lst[i]['w']]+lst[i]['v'])
    # 当所有物品的费用为非负时，二者应该是相等的
    return dp[j][-1]
    # return max(dp[j])


lst = [
    None,

    {'w': 3, 'v': 4},
    {'w': 4, 'v': 2},
    {'w': 2, 'v': 15},

    {'w': 9, 'v': 10},
    {'w': 5, 'v': 8},
]
W = 20
print(knapsack(W, lst))
