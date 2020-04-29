# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
# class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:


class Solution:
    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        length = mountain_arr.length()
        peak = self.findPeak(mountain_arr, length)
        res = self.findTargetLift(target, mountain_arr, peak)
        if res == -1:
            res = self.findTargetDrop(target, mountain_arr, peak)
        return res

    def findPeak(self, mountain_arr, length):
        left, right = 0, length-1
        while left < right:
            mid = left+(right-left)//2
            if mountain_arr.get(mid) < mountain_arr.get(mid+1):
                left = mid+1
            else:
                right = mid
        return left

    def findTargetLift(self, target, mountain_arr, peak):
        left, right = 0, peak
        while left <= right:
            mid = left+(right-left)//2
            midValue = mountain_arr.get(mid)
            if midValue == target:
                return mid
            elif midValue < target:
                left = mid+1
            else:
                right = mid-1
        else:
            return -1

    def findTargetDrop(self, target, mountain_arr, peak):
        left, right = peak, mountain_arr.length()-1
        while left <= right:
            mid = left+(right-left)//2
            midValue = mountain_arr.get(mid)
            if midValue == target:
                return mid
            elif midValue > target:
                left = mid+1
            else:
                right = mid-1
        else:
            return -1
