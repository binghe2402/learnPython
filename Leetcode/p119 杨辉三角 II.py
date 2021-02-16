from typing import List

# rowIndex从0开始


class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex < 2:
            return [1]*(rowIndex+1)
        row = [1, 1]
        for i in range(1, rowIndex):
            # newRow =
            row = [1]+[row[j]+row[j+1] for j in range(i)]+[1]
        return row


k = 3
s = Solution()
res = s.getRow(k)
print(res)
