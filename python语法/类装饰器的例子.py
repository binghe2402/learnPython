from functools import wraps

'''
作为类的实例，在
'''


class Counter:
    def __init__(self, func):
        self.func = func
        self.count = 0

    def __call__(self, *args, **kwargs):
        self.count += 1
        return self.func(*args, **kwargs)


@Counter                         # foo = Counter(foo)
def foo(x, y):
    return x*y


for i in range(10):
    print(foo(i, i+1))           # 通过__call__，调用foo实例

print(foo.count)  # 10
print('='*10)


class Counter2:
    def __init__(self):
        self.count = 0

    def __call__(self, fun):
        self.fun = fun
        self.count += 1

        @wraps(fun)
        def inner(*args):
            return self.fun(*args)
        return inner


@Counter2()
def foo2(x, y):
    return x*y


for i in range(10):
    print(foo2(i, i+1))

print(foo2.__name__)  # 10
print(Counter2().count)
