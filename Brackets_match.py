def bracketMatch(s):
    stack = []
    for bra in s:
        if bra in "({[":
            stack.append(bra)
        elif stack and ")}]".index(bra) == "({[".index(stack.pop()):
            pass
        else:
            return False
    if stack:
        return False
    else:
        return True


s = ''
print(bracketMatch(s))
