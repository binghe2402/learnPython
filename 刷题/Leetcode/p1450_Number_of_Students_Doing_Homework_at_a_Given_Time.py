from typing import List


class Solution:
    def busyStudent(self, startTime: List[int], endTime: List[int], queryTime: int) -> int:
        cnt = 0
        for i in range(len(startTime)):
            if startTime[i] <= queryTime <= endTime[i]:
                cnt += 1
        return cnt
