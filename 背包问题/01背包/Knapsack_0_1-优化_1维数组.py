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
由于dp[j][w] = max(dp[j-1][w], dp[j-1][w-lst[i]['w']]+lst[i]['v'])
需要用到前一行[j-1]。
又发现[w-lst[i]['w']],[w]， 一定不在[w]位置的右边
所以使用倒序遍历，这样就在计算写入dp[j][w]前，一维数组的[w]位置及左边，都是[j-1]的情况
另参考 https://leetcode-cn.com/problems/coin-lcci/solution/bei-bao-jiu-jiang-ge-ren-yi-jian-da-jia-fen-xiang-/367398/
'''


def knapsack(W, lst):
    # dp[w]
    dp = [0]*(W+1)
    # 如果要求最后恰好装满，则应初始化为
    # dp = [0]
    # dp += [float('-inf')]*W
    # 还没太明白，而且显然，此时解不是一定存在的
    for i in range(1, len(lst)):
        for w in range(W, lst[i]['w']-1, -1):
            # 下面直接退化到了w的取值范围中
            # if lst[i]['w'] > w:
            #     dp[w] = dp[w]
            dp[w] = max(dp[w], dp[w-lst[i]['w']]+lst[i]['v'])
    return dp[-1]
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
