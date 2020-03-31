import re


class expression:
    def __init__(self, expr):
        self.expr = re.findall(r'\(|\)|\*{2}|\+|\*|/|-|%|\w+', expr)

    def infix2postfix(self):
        postfix = []
        opStack = []
        op = ''
        priority = {'(': 1, ')': 1, '': 1,
                    '+': 2, '-': 2,
                    '*': 3, '/': 3,'%':3,
                    '^': 4, '**': 4}
        for char in self.expr:
            if char.isalnum():
                if postfix and postfix[-1].isalnum():
                    postfix.append(' ')
                postfix.append(char)
            elif char == '(':
                # 括号必须单独处理，不能利用直接其低优先级，否则会使'('前的运算符提前出栈
                opStack.append(char)
            elif char == ')':
                op = opStack.pop()
                while op != '(':
                    postfix.append(op)
                    op = opStack.pop()
            else:
                while opStack and priority[char] <= priority[opStack[-1]]:
                    op = opStack.pop()
                    postfix.append(op)
                    # op.append(char)
                else:
                    opStack.append(char)
        while opStack:
            postfix.append(opStack.pop())
            self.postfix_expr = ''.join(postfix)
        return self.postfix_expr

    def postfix_calculate(self, expr=None):
        if expr is None:
            expr = self.postfix_expr
        expr = re.findall(r'\w+|\*\*|\+|-|/|%|\*', expr)
        numStack = []
        # opStack = []
        for char in expr:
            if char.isalnum():
                numStack.append(char)
            elif char != ' ':
                num2 = numStack.pop()
                num1 = numStack.pop()
                numStack.append(eval(str(num1) + char + str(num2)))
        if len(numStack) == 1:
            return numStack[0]
        else:
            print("ERROR")

        # a+b*c+d   a b c*+ d+
        # a+b+c    a b+c+

    def show(self):
        print(self.expr)


aa, b, c, d, f = 1, 2, 3, 4, 5
exp = "(aa+b)*c+d/(f*d)**2-45*3%8"
# aaa=eval(exp)
bbb = (aa+b)*c+d/(f*d)**2-45*3%8
# print(aaa)
print(bbb)
# print(aaa==bbb)
e = expression(exp)  # ab+c*dfd*^/+
e.show()
ee = e.infix2postfix()
print(ee)
rer = e.postfix_calculate()
print(rer)
