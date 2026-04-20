class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l = 0
        r = len(s1)-1
        s1 = sorted(s1)
        while r < len(s2):
            s = sorted(s2[l:r+1])
            if s1 == s:
                return True
            l += 1
            r += 1
        return False