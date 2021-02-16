# HT13198 庄淼
n = int(input())
boy = [None for x in range(n)]
i = 1
for g in input().split():
    boy[int(g)-1] = i
    i += 1
print(*boy)
