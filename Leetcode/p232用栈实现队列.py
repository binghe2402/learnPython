class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack_head = []
        self.stack_tail = []

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.stack_head.append(x)

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        while self.stack_head:
            self.stack_tail.append(self.stack_head.pop())
        res = self.stack_tail.pop()
        # 其实不用再倒回去
        while self.stack_tail:
            self.stack_head.append(self.stack_tail.pop())
        return res

    def peek(self) -> int:
        """
        Get the front element.
        """
        while self.stack_head:
            self.stack_tail.append(self.stack_head.pop())
        res = self.stack_tail[-1]
        while self.stack_tail:
            self.stack_head.append(self.stack_tail.pop())
        return res

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return not bool(self.stack_head)


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
