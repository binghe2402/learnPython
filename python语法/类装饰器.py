'''
本篇需要添加更多细节
'''
'''
无参数
'''


class Foo:
    def __init__(self, func):
        self._func = func

    def __call__(self, *arg):
        print('class decorator runing')
        res = self._func(*arg)
        print('class decorator ending')
        return res


@Foo                    # bar = Foo(bar)
def bar(x):             # bar 成为一个 Foo(bar)实例
    print(x)
    print('bar')


bar(5)                  # 调用bar实例,触发__call__. 5被传入bar实例的__call__,然后又传入bar函数

'''
对于本身无参数的函数或方法，定义无参数装饰器，带参数调用
'''


class Foo:
    def __init__(self, func):
        self._func = func

    def __call__(self, x):
        print('class decorator runing')
        print(x)
        self._func()
        print('class decorator ending')


@Foo
def bar():                # bar 成为一个 Foo(bar)实例
    print('bar')


bar(5)                    # 调用bar实例,触发__call__

'''
定义时带参数
'''
from functools import wraps     # NOQA: E402


class Foo_1:
    def __init__(self, n):
        self.n = n

    def __call__(self, func):
        @wraps(func)
        def wrapped_function(*args, **kwargs):
            string = func.__name__ + " was called"
            print(string)
            self.notify()
            return func(*args, **kwargs)
        return wrapped_function

    def notify(self):
        print('hello %d' % (self.n))


@Foo_1(12)
def myfunc1(x):             # myfunc1成为一个Foo_(12)(myfunc1)可调用对象
    return x


s = myfunc1(1)
print(s)

#####################

'''
如果不发挥类更强大的功能，这样的实现可能用闭包更好
https://zhuanlan.zhihu.com/p/22229197
https://foofish.net/python-closure.html
'''

'''
参考阅读
https://zhuanlan.zhihu.com/p/65968462
https://foofish.net/magic-method.html
https://www.jianshu.com/p/e1d95c4e1697
'''
