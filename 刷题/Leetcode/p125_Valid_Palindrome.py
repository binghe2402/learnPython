class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        i, j = 0, len(s)-1
        while i < j:
            while i < len(s) and not s[i].isalnum():
                i += 1
            while j >= 0 and not s[j].isalnum():
                j -= 1
            if 0 <= i < j <= len(s)-1 and s[i] != s[j]:
                return False
            i += 1
            j -= 1
        else:
            return True


str = ".,"
s = Solution()
res = s.isPalindrome(str)
print(res)
