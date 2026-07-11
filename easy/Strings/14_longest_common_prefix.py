class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        if not strs:
            return ""
        if len(strs)==1:
            return "".join(strs)
        strs.sort()
        s1=strs[0]
        s2=strs[len(strs)-1]
        ans=[]
        for i in range(min(len(s1),len(s2))):
            if s1[i]!=s2[i]:
                return "".join(ans)
            ans.append(s1[i])
        return "".join(ans)      