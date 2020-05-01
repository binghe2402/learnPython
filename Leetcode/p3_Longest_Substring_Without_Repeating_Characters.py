class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        lst = set()
        i = j = 0
        maxlen = 0
        while j < len(s):
            if s[j] in lst:
                lst.remove(s[i])
                i += 1
            else:
                lst.add(s[j])
                j += 1
            if maxlen < len(lst):
                maxlen = len(lst)
        return maxlen


solution = Solution()
s = "pwwkew"
res = solution.lengthOfLongestSubstring(s)
print(res)
