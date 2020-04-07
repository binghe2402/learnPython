class Solution:
    def myAtoi(self, str: str) -> int:
        str = str.strip()
        if not str or ((not str[0].isdigit()) and (str[0] not in ('+', '-'))):
            return 0
        import re
        str = re.match(r'[\+-]?\d+', str)
        if str:
            str = int(str[0])
        else:
            return 0
        if str > 2**31-1:
            str = 2**31-1
        elif str < -2**31:
            str = -2**31
        return str


s = Solution()
str = "+"
d = s.myAtoi(str)
print(d)
