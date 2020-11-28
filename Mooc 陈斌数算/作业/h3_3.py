def wash(seq):
    n = 0
    stack = []
    for i in range(10):
        stack.append(i)
        while stack and stack[-1] == int(seq[n]):
            stack.pop()
            n += 1
        if stack and stack[-1] > int(seq[n]):
            return 'No'
    return 'Yes'


if __name__ == "__main__":
    print(wash(input()))
