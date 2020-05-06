''' 不一定谁快。前一个map再list快，后一个列表推导快 '''

import timeit


ss = 's="1 2 3 4 5 6 7 8 9 10".split()'

s1 = "a = list(map(int,s))"
s2 = 'b = [int(i) for i in s]'


t1 = timeit.timeit(stmt=s1, setup=ss, number=2000000)
t2 = timeit.timeit(stmt=s2, setup=ss, number=2000000)
print(t1)
print(t2)


ss = '''
with open('e://project_data//file_selector//random_list_b0000.txt', 'r') as random_list:
    select_lst = random_list.readlines()
'''

s1 = "a = list(map(lambda x:x.split(),select_lst))"
s2 = 'b = [i.split() for i in select_lst]'


t1 = timeit.timeit(stmt=s1, setup=ss, number=200)
t2 = timeit.timeit(stmt=s2, setup=ss, number=200)
print(t1)
print(t2)
