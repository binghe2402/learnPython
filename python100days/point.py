import math


class Point:
    _isnewpoint = False
    _ismove = False

    def __init__(self, x0=0, y0=0):
        self._x0 = x0
        self._y0 = y0

    def newpoint(self, x=None, y=None):
        self._x = x
        self._y = y
        self._isnewpoint = self._x is not None and self._y is not None

    def move(self, x=None, y=None):
        self._ismove = x is not None and y is not None
        if self._isnewpoint and (not self._ismove):
            print("x方向移动%f，y方向移动%f" % (self._x-self._x0, self._y-self._y0))
        elif self._ismove:
            self.newpoint(x+self._x0, y+self._y0)
        else:
            print("没有给定第二点，也没有给定位移")

    def distance(self):
        if self._isnewpoint:
            return math.sqrt((self._x-self._x0)**2+(self._y-self._y0)**2)


def main():
    A = Point(1, 2)
    A.move()

    B = Point(2, 3)
    B.move(-3, -4)
    dist_B = B.distance()
    print(dist_B)

    C = Point(-1, 3)
    C.newpoint(3, -4)
    C.move()


if __name__ == '__main__':
    main()
