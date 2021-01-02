from collections import deque


def func(mylist):
    # main = mylist[:]
    queue = [deque() for i in range(10)]
    flag = True
    n = 1
    while flag:
        flag = False
        for i in range(len(mylist)):
            d = mylist[i] // n % 10
            if d:
                flag = True
            queue[d].append(mylist[i])
        n *= 10
        mylist = []
        for x in queue:
            while x:
                mylist.append(x.popleft())
        # mylist = [x.popleft() for x in queue if len(x)]

    return mylist


mylist = eval(input())
print(func(mylist))
