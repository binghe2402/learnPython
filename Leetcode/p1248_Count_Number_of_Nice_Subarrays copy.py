from typing import List


class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        # 相当于nums是一个序列的一部分，nums[0]的前一个是奇数,nums[-1]后是一个奇数
        ind_odd = {-1: -1}
        j = 0
        for i in range(len(nums)):
            if nums[i] % 2:
                ind_odd[j] = i
                j += 1
        ind_odd[j] = len(nums)

        cnt = 0

        for i in range(len(ind_odd)-k-1):
            left, right = ind_odd[i], ind_odd[i+k-1]
            pre, nxt = ind_odd[i-1], ind_odd[i+k]
            cnt += (left-pre)*(nxt-right)

        return cnt


s = Solution()
nums = [66551, 12155, 74254, 25578, 71867, 43302, 68033, 17860, 845,
        46931, 39348, 90971, 50432, 83791, 62889, 98046, 15713, 20580,
        12018, 47181, 79611, 66700, 9392, 74854, 4399, 27356, 19428,
        52445, 78580, 46062, 36990, 60796, 48502, 60154, 96271, 84402,
        30678, 17756, 74576, 93855, 99342, 70654, 85675, 21669, 91922,
        37006, 87191, 76017, 6312, 41691, 14617, 17663, 74662, 36708,
        6137, 25984, 60304, 2831, 50352, 12354, 4076, 23326, 80547,
        51348, 84223, 6768, 75208, 16433, 3948, 46159, 16497, 79843,
        23833, 53023, 33879, 88215, 4992, 80152]
k = 5
res = s.numberOfSubarrays(nums, k)
print(res)
