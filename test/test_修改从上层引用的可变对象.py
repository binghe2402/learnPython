a = []


def fun():
    a += [3]
    a.append(1)


print(a)
fun()
print(a)
