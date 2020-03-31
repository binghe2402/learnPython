class Solution:
    def canThreePartsEqualSum(self, A) -> bool:
        summary = sum(A)
        part_sum = summary / 3.0
        part = 0
        if part != int(part):
            return False

        try:
            seg, i = self.ispart(A[self.ispart(A, part_sum)[1]+1:], part_sum)
        except ValueError:
            return False

        return seg

    def ispart(self, A, part_sum):
        part = 0
        for index, num in enumerate(A):
            part = part + num
            if part == part_sum:
                break
        if index == len(A)-1:
            raise ValueError("index end")
        else:
            return True, index
