''' 虽然转字符串遍历写起来方便，但是比正统的迭代求余要慢的多 '''

import timeit


ss = 'num=12345678\n' \
    'from functools import reduce'

s1 = 'num=str(num)\n' \
    'res=0\n'\
    'for n in num:\n'\
    '\tres+=int(n)'
s2 = 'res=0\n' \
    'while num:\n' \
    '\tnum,n=divmod(num,10)\n' \
    '\tres+=n'


t1 = timeit.timeit(stmt=s1, setup=ss, number=2000000)
t2 = timeit.timeit(stmt=s2, setup=ss, number=2000000)
print(t1)
print(t2)
