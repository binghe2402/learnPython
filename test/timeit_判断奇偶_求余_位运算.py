''' 求余好像更快 '''

import timeit


# ss = 'a = list(range(10000000))'
s1 = "for i in range(10):\n" \
    "\ti&1"
s2 = "for i in range(10):\n" \
    "\ti%2"


t1 = timeit.timeit(stmt=s1, number=20)
t2 = timeit.timeit(stmt=s2, number=20)

print(t1)
print(t2)
res = [i % 2 == i & 1 for i in range(10)]
print(res)
print(all(res))
