# HT13198 庄淼

n = int(input())
walnut = [int(x) for x in input().split()]
S = 0
max_w = 0
for n in range(len(walnut)):
    if walnut[n] > max_w:
        S += n*(walnut[n]-max_w)
        max_w = walnut[n]
    S += max_w-walnut[n]
print(S)
