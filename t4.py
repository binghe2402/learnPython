from functools import wraps


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
