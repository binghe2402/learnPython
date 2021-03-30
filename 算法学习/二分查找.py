'''
    内容参考
    二分查找有几种写法？它们的区别是什么？ - Jason Li的回答 - 知乎
    https://www.zhihu.com/question/36132386/answer/530313852
    当存在目标值，则求目标值。否则求大于目标值的最小值
    即求下界，x > value条件的最小x的位置，
'''

from typing import List


def binSearch_left(nums: List, val):
    left, right = 0, len(nums)
    while left < right:
        mid = left + (right-left)//2
        if nums[mid] == val:
            return mid
        elif nums[mid] < val:
            left = mid+1
        else:
            right = mid

    return left


def test():
    test_nums = [1, 2, 3, 4, 9, 9, 16, 27]
    test_val = 6
    res = binSearch_left(test_nums, test_val)
    print(res)


if __name__ == "__main__":
    test()
