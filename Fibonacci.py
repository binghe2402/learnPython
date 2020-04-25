def fib(n):

    a, b = 0, 1

    for _ in range(n):
        a, b = a+b, a
        yield a


print(list(fib(5)))
