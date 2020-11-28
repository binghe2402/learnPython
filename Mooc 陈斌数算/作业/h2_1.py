'''
# 直接算
n1 = int(input())
n2 = int(input())
# res = n1/n2 if n2 else 'NA'
print(("%.4f" % (n1/n2)) if n2 else 'NA')
'''
# 利用异常
n1 = int(input())
n2 = int(input())
try:
    # div = n1/n2
    div = "%.4f" % (n1/n2)
except ZeroDivisionError:
    div = 'NA'
print(div)
