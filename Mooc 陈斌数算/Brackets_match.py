'''括号匹配'''


def bracketMatch(s):
    '''利用栈做括号匹配'''
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


st = ''
print(bracketMatch(st))
