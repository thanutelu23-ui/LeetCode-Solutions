class Solution:
    def reverseWords(self, s: str) -> str:
        li=s.split()
        left=0
        right=len(li)-1
        while left<=right:
            li[left],li[right]=li[right],li[left]
            left+=1
            right-=1
        return " ".join(li)
        