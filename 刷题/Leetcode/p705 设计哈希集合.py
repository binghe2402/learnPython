class MyHashSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.base = 821
        self.hashmap = [[]]*self.base

    def add(self, key: int) -> None:
        hashkey = key % self.base

        for i in self.hashmap[hashkey]:
            if key == i:
                return
        self.hashmap[hashkey].append(key)

    def remove(self, key: int) -> None:
        hashkey = key % self.base
        for i in self.hashmap[hashkey]:
            if i == key:
                self.hashmap[hashkey].remove(key)

    def contains(self, key: int) -> bool:
        """
        Returns true if this set contains the specified element
        """
        hashkey = key % self.base
        for i in self.hashmap[hashkey]:
            if i == key:
                return True
        return False


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
