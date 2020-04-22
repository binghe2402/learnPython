from functools import lru_cache


# floored = set()
@lru_cache(None)
def flooring(n):
    # if n not in floored:
    #     floored.add(n)
    if n <= 1:
        return 1
    else:
        cnt = 0
        for i in range(1, min(n+1, 5)):
            cnt += flooring(n-i)
        return cnt
    # else:
    #     return 0
        # cnt = flooring(n-1)+flooring(n-2)+flooring(n-3)+flooring(n-4)


N = int(input())
print(flooring(N))
