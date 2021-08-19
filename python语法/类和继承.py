class Animal(object):
    run = True


class Dog(Animal):
    fly = False

    def __init__(self, age):
        self.age = age

    def sound(self):
        return "wang wang~"


# 实例化一个对象dog
dog = Dog(1)
# 查看dog对象的属性
# print ('dog.__dict__:',dog.__dict__)
# # 查看类Dog的属性
# print ('Dog.__dict__:',Dog.__dict__)
# # 查看类Animal的属性
print(dog.fly)
print(dog.age)
print(dog.run)
s = Animal.__getattribute__('run')
print(s)


import collections   # NOQA: E402


class print_queue(collections.deque):
    def get(self):
        if self:
            return self.pop()
        else:
            print("empty")

    def put(self, item):
        self.appendleft(item)


a = print_queue()
a.put(1)
a.put(2)
print(a.get())
print(a.get())
