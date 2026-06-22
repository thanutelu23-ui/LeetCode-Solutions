class Solution(object):
    def isPowerOfTwo(self, n):
        if n==1:
            return True
        i=1
        while i:
            r=2**i
            if r==n:
                return True
                break
            if r>n:
                break
            i+=1
        return False
        