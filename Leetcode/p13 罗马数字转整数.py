class Solution:
    def romanToInt(self, s: str) -> int:
        romanDigital = {'I': 1,
                        'V': 5,
                        'X': 10,
                        'L': 50,
                        'C': 100,
                        'D': 500,
                        'M': 1000}
        res = 0
        i = 0
        while i < len(s)-1:
            if romanDigital[s[i]] < romanDigital[s[i+1]]:
                res += romanDigital[s[i+1]]-romanDigital[s[i]]
                i += 2
            else:
                res += romanDigital[s[i]]
                i += 1
        if i == len(s):
            return res
        else:
            return res + romanDigital[s[i]]
