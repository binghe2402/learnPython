class Solution:
    def minWindow(self, s: str, t: str) -> str:
        i = 0
        j = 0
        cnt = dict.fromkeys(t, 0)
        for c in t:
            cnt[c] += 1
        min_len = s
        def check(cnt): return all(x <= 0 for x in cnt.values())
        while j <= len(s):
            if check(cnt):
                if s[i] in t:
                    if len(min_len) > j-i:
                        min_len = s[i:j]
                    cnt[s[i]] += 1
                i += 1
            else:
                if j < len(s) and s[j] in t:
                    cnt[s[j]] -= 1
                j += 1

        return min_len if i > 0 else ''


s = "AAB"
t = "AA"
sl = Solution()
res = sl.minWindow(s, t)
print(res)
