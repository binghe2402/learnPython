def get_yang(row):
    trigle = [[1], [1, 1]]
    for n in range(2, row):
        trigle = trigle + [[1]+[trigle[-1][i] + trigle[-1][i + 1]
                                for i in range(n-1)] + [1]]
    return trigle


def disp_yang(trigle):
    lenth = len(trigle)
    for i in range(lenth):
        print(" "*(lenth-i-1), end="")
        for num in trigle[i]:
            print(f'{num} ', end="")
        print("")


yang_trigle = get_yang(10)
disp_yang(yang_trigle)
