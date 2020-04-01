
from typing import List


class Solution:
    def maxDepthAfterSplit(self, seq: str) -> List[int]:
        if not seq:
            return seq
        StackA = []
        StackB = []
        distr = []
        for i in range(len(seq)):
            if seq[i] == "(":
                if StackA > StackB:
                    StackB.append('(')
                    distr.append(1)
                else:
                    StackA.append('(')
                    distr.append(0)
            else:
                if StackA > StackB:
                    StackA.pop()
                    distr.append(0)
                else:
                    StackB.pop()
                    distr.append(1)
        return distr


seq = "()(())()"

s = Solution()
distr = s.maxDepthAfterSplit(seq)
print(distr)
