class Solution:
    def isRectangleOverlap(self, rec1, rec2) -> bool:
        # x1,y2                  x2,y2

        #              x_1,y_2
        # x1,y1                  x2,y1
        x1, y1, x2, y2 = rec1
        x_1, y_1, x_2, y_2 = rec2

        is_out = x_2 <= x1 or x_1 >= x2 or y_1 >= y2 or y_2 <= y1
        return not is_out


if __name__ == "__main__":

    rec1 = [7, 8, 13, 15]
    rec2 = [10, 8, 12, 20]
    s = Solution()
    result = s.isRectangleOverlap(rec1, rec2)
    print(result)
