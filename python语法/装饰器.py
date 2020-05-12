'''
装饰器的目的:在执行目标函数(fun)时,增加额外功能(print)
'''


def printer(fun, *args):
    print('A')
    return fun(*args)


def fun_1(x, y):
    return x, y


d = printer(fun_1, 3, 5)
print(d)

'''
更实用化的装饰器
'''


def printer(fun):         # 传入待装饰的fun函数
    def wrap(*args):      # wrap函数对fun进行装饰
        print('A')        # 添加额外功能
        return fun(*args)  # 返回fun本身的结果。或装饰后的结果。
    return wrap           # 返回一个装饰了fun后得到的wrap函数


def a_fun(x, y):          # 一个实际的函数
    return x, y


a_fun_with_wrap = printer(a_fun)  # 传入a_fun,返回了装饰后的新函数
e = a_fun_with_wrap(3, 5)          # 如果只需要装饰后的函数,那a_fun = printer(a_fun)即可
print(e)

'''
更简洁的写法
'''


def printer(fun):
    def wrap(*args):
        print('A')
        return fun(*args)
    return wrap


@printer                  # @语法糖起到了上面 a_fun = printer(a_fun) 的作用
def a_fun(x, y):
    return x, y


e = a_fun(3, 5)
print(e)

'''
使用@wraps保留原函数的元信息
'''

from functools import wraps    # NOQA: E402
# 这条注释临时性的忽略了autopep8的E402，也就是import位置不在顶部


def decorator(fun):
    @wraps(fun)
    def printer(*a):
        print('A')
        return fun(*a)
    return printer


@decorator
def hello(x, y):
    return x, y


d = hello(3, 5)
print(d)

'''
带参数的装饰器,在外面再加一层函数。
这其实应该就是一个闭包
'''
from functools import wraps    # NOQA: E402,F811
# 这条注释临时性的又忽略了flake的F811，也就是重复import


def param(x, mode=1):
    def decorator(fun):
        @wraps(fun)
        def printer(*arg):
            if mode == 1:
                print('mode 1')
                return fun(*arg)
            else:
                print('mode is changed')
                print(x)
                return fun(*arg)
        return printer
    return decorator


@param(5, mode=2)
def func(x):
    return x**3+x**2


n = func(2)
print(n)


'''
参考阅读
https: // www.zhihu.com/question/26930016
https: // zhuanlan.zhihu.com/p/65968462
https://www.jianshu.com/p/fd746acbdf1e
闭包
https://zhuanlan.zhihu.com/p/22229197
https://foofish.net/python-closure.html
'''
