def printer(fun, *args):
    print('A')
    return fun(*args)


def fun(x, y):
    return x, y


d = printer(fun, 3, 5)

print(d)
