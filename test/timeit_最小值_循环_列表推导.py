''' 如果需要运算 直接循环求最小值比列表推导然后min()更快 '''

import timeit


ss = 'minlst=0\n' \
    'lst1=[x**2 for x in range(100)]\n' \
    'lst2=[1/(1+x) for x in range(100)]'
s1 = "minlst=min([lst1[i]+lst2[i] for i in range(100)])"
s2 = 'for i in range(100):\n' \
    '\tmintemp=lst1[i]+lst2[i]\n' \
    '\tif mintemp <minlst:minlst=mintemp'


t1 = timeit.timeit(stmt=s1, setup=ss, number=2000000)
t2 = timeit.timeit(stmt=s2, setup=ss, number=2000000)
print(t1)
print(t2)
