from functools import wraps


class Dec:
    def __init__(self):
        self.num = 0

    def __call__(self, fun):
        @wraps(fun)
        def note(*args):
            print("note")
            return fun(*args)
        return note


@Dec()
def plus(x, y):
    return x+y


print(plus(3, 5))
