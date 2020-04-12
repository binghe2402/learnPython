'''
参考知乎
https://zhuanlan.zhihu.com/p/27643991 和
文档
https://docs.python.org/zh-cn/3/library/functools.html#functools.singledispatch
'''


import functools
@functools.singledispatch
def typecheck():
    pass

# 两种写法，一种用函数参数注解，另一种作为register的参数
@typecheck.register
def _(text: int):
    print(type(text))
    print("int--")


@typecheck.register(str)
def _(text):
    print(type(text))
    print("str--")


@typecheck.register(list)
def _(text):
    print(type(text))
    print("list--")


a = 1
typecheck(a)
