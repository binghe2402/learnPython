''' 如果需要运算 直接循环求最小值比列表推导然后min()更快 '''

import timeit


ss = 's="1 2 3 4 5 6 7 8 9 10".split()'

s1 = "a = list(map(int,s))"
s2 = 'b = [int(i) for i in s]'


t1 = timeit.timeit(stmt=s1, setup=ss, number=2000000)
t2 = timeit.timeit(stmt=s2, setup=ss, number=2000000)
print(t1)
print(t2)
