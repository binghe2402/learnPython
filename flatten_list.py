def flatten(nested_list):
    for item in nested_list:
        if isinstance(item, (list, tuple)):
            for sub_item in flatten(item):
                yield sub_item
        else:
            yield item


print(
    list(flatten([2, 3, 4, [[5, 6]], ['a', 'g'], [6, [8, [9, [[[0]], 6]], 8]]])))
