class Solution:
    def largestOddNumber(self, num: str) -> str:
        idx=-1
        for i in range(len(num)-1,-1,-1):
            if int(num[i])%2==1:
                idx=i
                break
        i=0
        while i<=idx and num[i]=='0':
            i+=1
        return num[i:idx+1]