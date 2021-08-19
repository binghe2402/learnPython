from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []
        intervals.sort()
        merged = []
        left, right = intervals[0]
        for i in range(1, len(intervals)):
            if right >= intervals[i][0]:
                if intervals[i][1] > right:
                    right = intervals[i][1]
            else:
                merged.append([left, right])
                left = intervals[i][0]
                right = intervals[i][1]
        merged.append([left, right])
        return merged
