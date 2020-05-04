def gcd(a, b):
    c = a % b
    if c == 0:
        return b
    else:
        return gcd(b, c)


d = gcd(3, 5)
print(d)
