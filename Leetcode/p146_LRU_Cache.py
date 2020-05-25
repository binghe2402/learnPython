class LRUCache:
    class listNode:
        def __init__(self, key, val):
            self.val = val
            self.key = key
            self.next = None
            self.pre = None

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.data = {}
        self.dataLinkBegin = self.listNode(None, None)
        self.dataLinkEnd = self.listNode(None, None)
        self.dataLinkBegin.next = self.dataLinkEnd

    def get(self, key: int) -> int:
        if key in self.data:
            res = self.data[key].val
            self.data[key].pre.next = self.data[key].next
            self.data[key].next.pre = self.data[key].pre
            self.data[key].next = self.dataLinkBegin.next
            self.data[key].next.pre = self.data[key]
            self.data[key].pre = self.dataLinkBegin
            self.dataLinkBegin.next = self.data[key]
            return res
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        # Your LRUCache object will be instantiated and called as such:
        # obj = LRUCache(capacity)
        # param_1 = obj.get(key)
        # obj.put(key,value)

        if key in self.data:
            self.data[key].val = value
            self.data[key].pre.next = self.data[key].next
            self.data[key].next.pre = self.data[key].pre
            self.data[key].next = self.dataLinkBegin.next
            self.data[key].next.pre = self.data[key]
            self.data[key].pre = self.dataLinkBegin
            self.dataLinkBegin.next = self.data[key]
        else:
            if len(self.data) == self.capacity:
                del self.data[self.dataLinkEnd.pre.key]
                self.dataLinkEnd.pre.pre.next = self.dataLinkEnd
                self.dataLinkEnd.pre = self.dataLinkEnd.pre.pre

            self.data[key] = self.listNode(key, value)
            self.data[key].pre = self.dataLinkBegin
            self.data[key].next = self.dataLinkBegin.next
            self.dataLinkBegin.next = self.data[key]
            self.data[key].next.pre = self.data[key]
