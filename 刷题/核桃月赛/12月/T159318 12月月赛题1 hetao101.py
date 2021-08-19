# HT13198 庄淼

string = input()
lst = list("hetao101")
for c in string:
    if lst == []:
        break
    if c in lst:
        lst.remove(c)

print("so sad!" if lst else "hetao101")
