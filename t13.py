from timeit import Timer

# 四种生成前n个整数列表的方法


def test1():

    lst = []

    for i in range(1000):

        lst += [i]

# 首先是循环连接列表（+）方式生成


def test2():

    lst = []

    for i in range(1000):

        lst.append(i)

# 然后是用append方法添加元素生成


def test3():

    lst = [i for i in range(1000)]

# 接着用列表推导式来做


def test4():

    lst = list(range(1000))

# 最后是range函数调用转成


t1 = Timer("test1()", "from __main__ import test1")

print("concat %f seconds/n" % t1.timeit(number=1000))

t2 = Timer('test2()', 'from __main__ import test2')

print('append %f seconds/n' % t2.timeit(number=1000))

t3 = Timer('test3()', 'from __main__ import test3')

print('comprehension %f seconds/n' % t3.timeit(number=1000))

t4 = Timer('test4()', 'from __main__ import test4')

print('range %f seconds/n' % t4.timeit(number=1000))
