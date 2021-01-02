def func(S):
    minS = ss = S

    for i in S:
        ss = ss[1:]+ss[0]
        if ss < minS:
            minS = ss
    return minS


S = eval(input())
print(func(S))
