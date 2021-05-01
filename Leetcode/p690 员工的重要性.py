from typing import List
# Definition for Employee.


class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates


class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        emps = dict([(i.id, i) for i in employees])
        imp = 0
        sub = [id]
        while sub:
            i = sub.pop()
            imp += emps[i].importance
            sub.extend(emps[i].subordinates)

        return imp
