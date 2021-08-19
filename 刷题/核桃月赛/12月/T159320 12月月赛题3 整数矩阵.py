# HT13198 庄淼

n, m, k = (int(x) for x in input().split())
mm = m//2
mat = []
max_lst = []
rst_lst = []
for i in range(n):
    mat.append(list(sorted([int(x) for x in input().split()], reverse=1)))
    max_lst += mat[-1][:mm]
    rst_lst += mat[-1][mm:]
summary = sum(max_lst)
mod = summary % k
if mod:
    print(summary)
else:
    max_ele = max(max_lst)
    if (max_ele-mod) in rst_lst:
