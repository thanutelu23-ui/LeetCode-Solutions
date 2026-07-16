from itertools import permutations
class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        result=list(permutations(nums))
        return result
        