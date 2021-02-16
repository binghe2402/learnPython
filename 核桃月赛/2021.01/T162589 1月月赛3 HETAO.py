# HT13198 庄淼

import re
s = re.sub(r"[^HETAO]", "", input())
t = "HETAO"

i = j = 0
while s[i] != "H":
    i += 1
j = i
cnt = 0
while s[j] != "E":
    if s[j] == "H":
        cnt += 1
    j += 1
i = j

N = cnt
cnt = 0

while s[j] != "T":
    if s[j] == "E":
        cnt += 1
    j += 1
i = j
N *= cnt

print(s)
