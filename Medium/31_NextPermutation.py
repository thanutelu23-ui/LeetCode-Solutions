class Solution:
    def nextPermutation(self, nums: list[int]) -> None:
        n=len(nums)
        idx=-1
        for i in range(n-2,-1,-1):
            if nums[i]<nums[i+1]:
                idx=i
                break
        if idx==-1:
            nums.reverse()
            return nums
        for i in range(n-1,idx,-1):
            if nums[i]>nums[idx]:
                nums[i],nums[idx]=nums[idx],nums[i]
                break
        nums[idx+1:]=nums[idx+1:][::-1]
        return nums
        