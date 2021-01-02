# HT13198 庄淼

# import psutil
# import os
n, q = (int(x) for x in input().split())
an = [int(x) for x in input().split()]
# n, q = 200000, 1
# an = list(range(1, 200001))
for i in range(q):
    l, r = (int(x) for x in input().split())
    # l, r = 1, len(an)
    if (r-l+1) % 2:
        print("NO")
    else:
        temp = set()
        for j in range(l-1, r):
            if an[j] in temp:
                temp.remove(an[j])
            else:
                temp.add(an[j])
        print('NO' if temp else "YES")
        # print(temp)
        # print(u'当前进程的内存使用：%.4f MB' %
        #       (psutil.Process(os.getpid()).memory_info().rss / 1024 / 1024))
