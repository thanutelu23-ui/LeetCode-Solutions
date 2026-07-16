class Solution:
    def frequencySort(self, s: str) -> str:
        freq={}
        ans=""
        for i in s:
            freq[i]=freq.get(i,0)+1
        sorted_freq = dict(sorted(freq.items(), key=lambda x: x[1], reverse=True))
        for i,c in sorted_freq.items():
            ans+=i*c
        return ans
        