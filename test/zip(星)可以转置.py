x = [1, 2, 3]
y = [4, 5, 6]
z = [7, 8, 9]

xyz = list(zip(x, y, z))
print(xyz)
print(*xyz)
print(list(zip(*xyz)))
