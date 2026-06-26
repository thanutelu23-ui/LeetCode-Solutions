class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        mpp = {}

        for i, num in enumerate(nums):
            if target - num in mpp:
                return [mpp[target - num], i]
            mpp[num] = i

        return [-1, -1]
        