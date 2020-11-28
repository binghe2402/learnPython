# bracket_seq = input()

def match_bracket(bracket_seq):
    stack = []
    match_key = {'(': ')', '[': ']', '{': '}'}
    for i in bracket_seq:
        if i in '([{':
            stack.append(i)
        else:
            if not stack or match_key[stack.pop()] != i:
                return False
    return not(bool(stack))


if __name__ == "__main__":
    print(match_bracket(input()))
