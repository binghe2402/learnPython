def flatten(lst):
    flt_lst = []
    for element in lst:
        if type(element) is list:
            flt_lst.extend(flatten(element))
        else:
            flt_lst.append(element)
    return flt_lst


lst = [1, [[2], [3, [4, [5, [6]], 7], [8]], [[6]]]]
ll = flatten(lst)
print(ll)
