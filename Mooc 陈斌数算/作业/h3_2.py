def samegame(seq):
    stack = [seq[0]]
    for i in seq[1:]:
        if stack and i == stack[-1]:
            stack.pop()
        else:
            stack.append(i)
    return ''.join(stack) if stack else None


if __name__ == "__main__":
    print(samegame(input()))
