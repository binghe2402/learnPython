class Solution:
    def validPalindrome(self, s: str) -> bool:

        def isPalindrome(s):
            i, j = 0, len(s)-1
            while i < j:
                if s[j] != s[i]:
                    return False
                else:
                    i += 1
                    j -= 1
            return True

        i, j = 0, len(s)-1
        while i < j:
            if s[j] != s[i]:
                return isPalindrome(s[i+1:j+1]) or isPalindrome(s[i:j])
            else:
                i += 1
                j -= 1
        return True


str = "abc"
s = Solution()
res = s.validPalindrome(str)
print(res)
