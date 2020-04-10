''' 测试字符串规模对字符串连接  + 和 +=  的影响'''

import timeit
# def fun1(y):

#     return x

# def fun2(y):
#     if y > 1:
#         x = y
#     else:
#         x = 0
#     return x

ss = 'y ,x = "bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb", "aaaaaaasssssssssssssssssssssssssssaaaaa"'
s1 = "x += y"
s2 = "x = x + y"

t1 = timeit.timeit(stmt=s1, setup=ss, number=200000)
t2 = timeit.timeit(stmt=s2, setup=ss, number=200000)
print(t1)
print(t2)
