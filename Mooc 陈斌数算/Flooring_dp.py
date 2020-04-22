
def flooring(n):
    # if n not in floored:
    #     floored.add(n)
    cnt = [0]*(n+1)
    cnt[0] = 1
    cnt[1] = 1
    for j in range(n+1):
        for i in range(1, min(j+1, 5)):
            cnt[i] += cnt[j-i]
    return cnt[-1]


N = int(input())
print(flooring(N))
