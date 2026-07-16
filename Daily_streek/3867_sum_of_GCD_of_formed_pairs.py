import math
class Solution:
    def gcdSum(self, nums: list[int]) -> int:
        mx=0
        prefix=list()
        for i in nums:
            mx=max(mx,i)
            prefix.append(math.gcd(mx,i))
        prefix.sort()
        left=0
        right=len(prefix)-1
        ans=0
        while left<right:
            ans+=math.gcd(prefix[left],prefix[right])
            left+=1
            right-=1
        return ans
        