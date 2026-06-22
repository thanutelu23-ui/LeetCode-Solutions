class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        unique=list(dict.fromkeys(nums))
        k=len(unique)
        nums[:k]=unique
        return k