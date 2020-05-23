''' map和生成器推导几乎一样最快 但是似乎还是map快一点点 '''

import timeit


ss = 's="1234567890-=qwertyuiop[]\asdfghjkl;zxcvbnm,./"\n' \
    'cnt = {c:0 for c in s}'

s1 = 'all(map(lambda x:x >0 , cnt.values()))'

s2 = 'all([x >0 for x in cnt.values()])'

s3 = 'all([cnt[x] >0 for x in cnt])'

s4 = 'all((x >0 for x in cnt.values()))'


t1 = timeit.timeit(stmt=s1, setup=ss, number=20000000)
t2 = timeit.timeit(stmt=s2, setup=ss, number=20000000)
t3 = timeit.timeit(stmt=s3, setup=ss, number=20000000)
t4 = timeit.timeit(stmt=s4, setup=ss, number=20000000)
print(t1)
print(t2)
print(t3)
print(t4)
