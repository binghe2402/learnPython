''' 逻辑运算小胜 但微乎其微 '''

import timeit


ss = 'a=1\nb=0'
s1 = "c = a and 2\n"\
    "d = b and 2"
s2 = 'if a:\n' \
    '\tc=2\n' \
    'else:\n'\
    '\tc=a\n'\
    'if b:\n'\
    '\td=2\n'\
    'else:\n'\
    '\td=b'
s3 = 'c=2 if a else a\n'\
    'd=2 if b else b'


t1 = timeit.timeit(stmt=s1, setup=ss, number=200000000)
t2 = timeit.timeit(stmt=s2, setup=ss, number=200000000)
t3 = timeit.timeit(stmt=s3, setup=ss, number=200000000)
print(t1)
print(t2)
print(t3)
