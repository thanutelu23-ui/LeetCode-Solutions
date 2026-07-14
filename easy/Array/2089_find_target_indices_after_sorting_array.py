class Solution:
    def targetIndices(self, nums: list[int], target: int) -> list[int]:
        nums.sort()
        indexes=[]
        indexes=[i for i,x in enumerate(nums) if x==target]
        return indexes

        