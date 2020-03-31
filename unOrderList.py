class UnOrderList:
    def __init__(self):
        self.head = None

    def add(self, new):
        newnode = Node(new)
        newnode.next = self.head
        self.head = newnode


class Node:
    def __init__(self, data):
        self.__data = data
        self.__next = None

    @property
    def next(self):
        return self.__next

    @next.setter
    def next(self, nextnode):
        self.__next = nextnode

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, data):
        self.__data = data
