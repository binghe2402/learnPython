N = int(input())
isBadVersion = eval(input())


def firstBadVersion(n):
    left, right = 0, N+1
    while left < right:
        mid = left + (right-left)//2
        if isBadVersion(mid):
            right = mid
        else:
            left = mid+1
    return left


print(firstBadVersion(N))
