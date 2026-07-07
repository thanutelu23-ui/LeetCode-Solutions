class Solution:
    def reverseVowels(self, s: str) -> str:
        v="AEIOUaeiou"
        n=len(s)
        left=0
        right=n-1
        s=list(s)
        while left<=right:
            if s[left] not in v:
                left+=1
            elif s[right] not in v:
                right-=1
            else:
                s[left],s[right]=s[right],s[left]
                left+=1
                right-=1
        return "".join(s)
        