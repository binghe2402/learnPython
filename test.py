class Parent:        # 定义父类
    parentAttr = 100

    def __init__(self, a0, b0):
        self.a = a0
        self.b = b0

    def parentMethod(self):
        print('调用父类方法')

    def fun(self):
        self.parentMethod()


c = Parent(1, 2)          # 实例化子类
print(c.fun())
