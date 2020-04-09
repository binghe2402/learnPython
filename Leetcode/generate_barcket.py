'''
22. 括号生成
https://leetcode-cn.com/problems/generate-parentheses/
'''
from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        lengrh = 2*n

        def generate(lengrh):
            if lengrh == 1:
                return [['(', 1, 0]]
            else:
                brs = []
                for br in generate(lengrh-1):
                    if br[1] < n:
                        brs += [[br[0] + '(', br[1]+1, br[2]]]
                    if br[1] > br[2]:
                        brs += [[br[0] + ')', br[1], br[2]+1]]
                return brs
        return [br[0] for br in generate(lengrh)]


n = 3
s = Solution()
ans = s.generateParenthesis(n)
print(ans)
