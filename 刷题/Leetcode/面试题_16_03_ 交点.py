from typing import List


class Solution:
    def intersection(self,
                     start1: List[int], end1: List[int],
                     start2: List[int], end2: List[int]) -> List[float]:
        points = []
        for x in [start1, end1, start2, end2]:
            if x in points:
                return x
            else:
                points.append(x)

        def getLinePara(point1, point2):
            delta_x = point1[0]-point2[0]
            delta_y = point1[1]-point2[1]
            delta_c = point1[0]*point2[1]-point2[0]*point1[1]

            # k = delta_y/delta_x
            # b = delta_c/delta_x

            return delta_y, -delta_x, delta_c  # , k, b

        def check_range(x, y, point1, point2):
            return (x-point1[0])*(x-point2[0]) <= 0 \
                and (y-point1[1])*(y-point2[1]) <= 0

        A1, B1, C1 = getLinePara(start1, end1)
        A2, B2, C2 = getLinePara(start2, end2)

        if A1 * B2 == A2 * B1:
            if A1*C2 != A2*C1:
                return []
            else:
                points = sorted([start1, end1, start2, end2])
                if (points[0] in [start1, end1]) ^ (points[1] in [start1, end1]):
                    return points[1]
                else:
                    return []

        else:
            y = (C2*A1-C1*A2)/(B1*A2-B2*A1)
            x = (B1*C2-B2*C1)/(B2*A1-B1*A2)

            return [x, y] \
                if check_range(x, y, start1, end1) \
                and check_range(x, y, start2, end2) \
                else []


s = Solution()
x1 = [0, 0]
y1 = [0, 1]
x2 = [0, 2]
y2 = [0, 3]

res = s.intersection(x1, y1, x2, y2)

print(res)
