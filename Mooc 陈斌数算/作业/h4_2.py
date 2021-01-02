'''
方法1
def func(mylist):
    queue = []
    output = []
    for event in mylist:
        # queue是符合范围的事件队列。output中储存个数，每个个数都是单元素的list。
        # 当输入事件不同时，新的计数单元素list是从新的[None]而来
        # 当输入两个相同的事件时，新的计数单元素list是从上一个事件的计数list而来，因此可以一起被修改
        if queue and event == queue[0]:
            output.append(output[-1])
        else:
            output.append([None])
        queue.insert(0, event)
        while queue[-1] < event-10000:
            queue.pop()

        output[-1][0] = len(queue)
    return [x[0] for x in output]


mylist = eval(input())
print(func(mylist))
'''

from collections import deque


def func(mylist):

    queue = deque()
    output = []
    duplicate = 0
    for i in range(len(mylist)):
        queue.append(mylist[i])
        while queue[0] < mylist[i]-10000:
            queue.popleft()
        cnt = len(queue)
        if duplicate:
            duplicate -= 1
        else:
            for j in range(i+1, len(mylist)):
                if mylist[j] == mylist[i]:
                    duplicate += 1
                else:
                    break
        output.append(cnt+duplicate)

    return output


mylist = eval(input())
print(func(mylist))
