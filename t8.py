# 把property当成描述器一样用是不可行的，没有效果
# 下面的测试中，利用@property将Int()的setter和getter均设置为返回定值，但下面的Point仍返回输入值


class Int:
    def __init__(self):
        self._Int = None

    @property
    def Int(self):
        """I'm the 'Int' property."""
        return 33

    @Int.setter
    def Int(self, value):
        if not isinstance(value, int):
            raise TypeError('Expected an int')
        # instance.__dict__[self.name] = value
        self._Int = 22

    @Int.deleter
    def Int(self):
        del self._Int

    def __str__(self):
        return "asd"


class Point:
    x = Int()
    y = Int()

    def __init__(self, x, y):
        self._x = x
        self._y = y

    def __str__(self):
        return "point(%d,%d)" % (self._x, self._y)


a = Int()

a.x = 1
print(a)

p = Point(3, 7.5)
print(p)
