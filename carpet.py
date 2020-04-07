def carpet(N, char):
    pattern = [[char, char, char],
               [char, ' '*len(char), char],
               [char, char, char]]
    for i in range(N):
        for j in range(N):
            drawCarpet(i, j, pattern, N)
        print()


def drawCarpet(i, j, pattern, N):
    if i < 3 and j < 3:
        print(pattern[i][j], end='')
    else:
        N //= 3
        if N <= i < 2*N and N <= j < 2*N:
            print(pattern[1][1])
        else:
            drawCarpet(i % N, j % N, pattern, N)


n = int(input())
c = input()
carpet(n, c)
