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


def binSearch_right(nums: List, val):
    # 当存在目标值，则求目标值。否则求小于目标值的最大值
    即求下界，x > value条件的最小x的位置，
    left, right = -1, len(nums)-1
    while left < right:
        mid = right - (right-left)//2
        if nums[mid] == val:
            return mid
        elif nums[mid] < val:
            left = mid
        else:
            right = mid-1

    return right


def binSearch(nums: List, val):  # 参考《算法图解》p7
    left, right = 0, len(nums)-1
    while left <= right:
        mid = left+(right-left)//2
        if nums[mid] == val:
            return mid
        if nums[mid] < val:
            right = mid-1
        else:
            left = mid + 1
    return None


def test():
    test_nums = [0, 1, 2, 3, 9, 9, 16, 27]
    test_val = 9
    res = binSearch_right(test_nums, test_val)
    print(res)


if __name__ == "__main__":
    test()
