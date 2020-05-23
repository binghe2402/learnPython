class Solution:
    def minWindow(self, s: str, t: str) -> str:
        i = 0
        j = 0
        # # len(t)   # 短的肯定不是   # 不行，必须从0开始，要不然不知道0:len(t)之间是什么
        cnt = dict.fromkeys(t, 0)
        for c in t:
            cnt[c] += 1
        # min_len = len(s)
        pos = (0, len(s))
        # distance是窗口中字符串偏离t的程度，也就是有多少个字符不同
        # 初始窗口为s[0:0]，也就是空，因此初始distance为len(t)，即全部不同
        distance = len(t)
        # 对于计数cnt
        # 如果新加入的s[j]在t中(为解释方便称这个字符为 t[k])，就把对应的计数 cnt[s[j]] -= 1，
        # 当计数全为0，说明这一段包含了所有的t
        # 计数减到0之前，每次都是窗口字符串向 t 靠近，因此也把distance -= 1
        # 如果cnt[s[j]]<=0，则该项对distance不再有贡献（之后加入的相同t[k]字符都是多余的）
        # 当新离开的s[i]在t中，对应计数+1
        # 如果cnt[s[i]]<0,则该项对distance没有贡献（移除窗口中多余的t[k]字符，不影响distance）
        # 如果cnt[s[i]]>0,实际上不会出现这种情况。因为在cnt[s[i]]==0是,distance+1,就又进入移动j了
        # 同理，distance不会出现负值

        while j < len(s):
            if distance:
                # 当 distance > 0,向右扩大窗口
                if s[j] not in t:
                    j += 1
                    continue
                if cnt[s[j]] > 0:
                    distance -= 1
                cnt[s[j]] -= 1
                j += 1
            while distance == 0:
                # 找到后立刻要开始缩小窗口，不要放在下一次循环，
                # 否则还要额外处理j，以免j==len(s)之间退出
                # 或者又+1跑了扩大窗口，比较麻烦
                if s[i] not in t:
                    i += 1
                    continue
                if pos[1]-pos[0] > j-i:
                    pos = (i, j)
                    # min_len = s[i:j]
                if cnt[s[i]] == 0:
                    distance += 1
                cnt[s[i]] += 1
                i += 1

        return s[pos[0]:pos[1]] if i > 0 else ''


s = "AB"
t = "A"
sl = Solution()
res = sl.minWindow(s, t)
print(res)
