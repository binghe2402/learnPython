def fun_1(lst_1 = []):
    print(lst_1)
    return lst_1
res = fun_1()     #输出   []

res.append(1)

fun_1()           #输出   [1]