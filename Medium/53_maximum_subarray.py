from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxi = nums[0]
        add = 0

        for i in range(len(nums)):
            add += nums[i]
            maxi = max(maxi, add)

            if add < 0:
                add = 0

        return maxi