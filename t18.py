# 测试方法继承

import collections


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
