class Solution:
    def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:
        # if (max(ax1, ax2) <= min(bx1, bx2) or min(ax1, ax2) >= max(bx1, bx2) or max(ay1, ay2) <= min(by1, by2) or min(ay1, ay2) >= max(by1, by2)):
        #     return 0

        def line(a1, a2, b1, b2):
            if a2 <= b1 or a1 >= b2:
                return 0

            # if a1 <= b1:
            #     if b2 > a2:
            #         length = a2-b1
            #     else:
            #         length = b2-b1
            # else:
            #     if b2 > a2:
            #         length = a2-a1
            #     else:
            #         length = b2-a1
            length = min(a2, b2)-max(a1, b1)
            return length
        x = line(ax1, ax2, bx1, bx2)
        y = line(ay1, ay2, by1, by2)
        res = (ax2-ax1)*(ay2-ay1)+(bx2-bx1)*(by2-by1)-x*y
        return res
