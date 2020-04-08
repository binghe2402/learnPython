"""
模拟打印机任务
学生概率的产生打印任务
打印机按照均匀的速度执行打印任务
计算打印任务的平均等待时间
"""

import collections
import random


class Printer:
    """打印机类"""
    printing = None    # 正在打印的任务

    # 创建打印队列类。继承collections.deque双端队列。
    class queue(collections.deque):
        """打印队列"""

        def get(self):
            ''' get方法从队列中取出任务。仅当队列非空时执行。'''
            return self.pop()

        def put(self, item):
            '''put方法添加任务到队首'''
            self.appendleft(item)

    # 初始化，设置打印模式。 Fast模式打印速度为10页/min   Normal模式为5p/min
    # 如果打印速度被显示指定，则忽略打印模式

    def __init__(self, printMode='Normal', *, printSpeed=None):
        Mode = {'Normal': 5,
                'Fast': 10}
        self.printSpeed = printSpeed if printSpeed else Mode[printMode]
        self.print_queue = self.queue()

    def doPrint(self, t):
        '''
         执行打印，若无打印中任务，则从打印队列获取新的任务
         获取任务后，printing为Task()实例。当其printTime属性不为0时，bool为真
        '''
        if self.printing:                               # printing为真，有任务正在打印
            self.printing.printTime -= 1
        else:                                           # 没有正在打印
            try:
                self.printing = self.startPrint(self.print_queue.get())
            except IndexError:
                return None
            else:
                wait_time = t - self.printing.generatedTime
                self.doPrint(t)
                return wait_time

    def startPrint(self, printTask):
        ''' 启动新打印，设置打印时间'''
        printTask.printTime = printTask.page * 60 // self.printSpeed
        return printTask

    def receiveTask(self, task):
        ''' 接受打印任务'''
        self.print_queue.put(task)


class Student:
    '''学生类用于产生任务'''

    def __init__(self, n):
        self.n = n

    def gerenateAtask(self, t):
        '''产生任务'''
        r = random.randrange(0, self.n)
        if not r:
            new_task = Task(t)
            # print(t)
            return new_task

        return None


class Task:
    ''' 任务类'''

    def __init__(self, t):
        self.generatedTime = t
        self.page = random.randint(1, 20)
        self.printTime = 1

    def __bool__(self):
        return bool(self.printTime)


def simPrintprocess(time, printMode='Normal', *, printSpeed=None):
    '''模拟打印流程'''
    wait_time_list = []
    student = Student(180)
    printer = Printer(printMode=printMode, printSpeed=printSpeed)
    for t in range(time):
        task = student.gerenateAtask(t)
        if task:
            printer.receiveTask(task)
        wait_time = printer.doPrint(t)
        if wait_time is not None:
            wait_time_list.append(wait_time)

    tot_time = sum(wait_time_list)
    ave_time = tot_time / len(wait_time_list)

    print("total time  : %ds" % tot_time)
    print("average time: %ds" % ave_time)

    if printer.printing:
        print("Still printing")
    if printer.print_queue:
        print("%d is left" % len(printer.print_queue))


if __name__ == "__main__":
    simPrintprocess(3600)
