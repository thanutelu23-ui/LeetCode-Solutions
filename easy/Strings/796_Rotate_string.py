class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if len(s)!=len(goal):
            return False
        rotate=s+s
        if goal in rotate:
            return True
        return False
        