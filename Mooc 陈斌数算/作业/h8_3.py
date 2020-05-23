'''直接取余做hash二次探测做rehash的散列表'''
import bisect


# def binfind(nums, n):
#     left, right = 0, len(nums)
#     while left < right:
#         mid = left+(right-left)//2
#         if nums[mid] == n:
#             return mid
#         elif nums[mid] < n:
#             left = mid + 1
#         else:
#             right = mid
#     return left

# def binfind(nums, n):
#     left, right = 0, len(nums)-1
#     while left <= right:
#         mid = left+(right-left)//2
#         if nums[mid] == n:
#             return mid
#         elif nums[mid] < n:
#             left = mid+1
#         else:
#             right = mid-1
#     return left


def createHashTable(n):
    primeList = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]

    n = bisect.bisect_left(primeList, n)
    return [None]*primeList[n]


def insertNumbers(table, nums):
    pos = []
    for n in nums:
        start = i = n % len(table)
        k = 1
        while table[i] is not None and table[i] != n:
            i = (i+2*k-1) % len(table)
            k += 1
            if i == start:
                pos.append('-')
                break
        else:
            table[i] = n
            pos.append(i)
    return pos


n = int(input())
nums = list(map(int, input().split()))
table = createHashTable(n)
res = insertNumbers(table, nums)
print(('%s '*len(res)).strip() % tuple(i for i in res))
