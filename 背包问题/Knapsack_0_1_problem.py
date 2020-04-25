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


lst = [
    None,

    {'w': 3, 'v': 4},
    {'w': 4, 'v': 8},
    {'w': 2, 'v': 3},

    {'w': 9, 'v': 10},
    {'w': 5, 'v': 8},
]
W = 20
print(knapsack(W, lst))
