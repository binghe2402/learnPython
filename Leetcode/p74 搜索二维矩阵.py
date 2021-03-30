from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def binSearchRight(nums, val):

            left, right = -1, len(nums)-1
            if right == 0:
                return right

            while left < right:
                mid = right-(right-left)//2
                if nums[mid] == val:
                    return mid
                if nums[mid] < val:
                    left = mid
                else:
                    right = mid-1
            return right

        # colVec_left = [vec[0] for vec in matrix]
        row_n = binSearchRight([vec[0] for vec in matrix], target)
        if target == matrix[row_n][0]:
            return True
        # rowVec = matrix[row_n]

        return matrix[row_n][binSearchRight(matrix[row_n], target)] == target


s = Solution()
matrix = [[1, 4]]
target = 4
res = s.searchMatrix(matrix, target)
print(res)
