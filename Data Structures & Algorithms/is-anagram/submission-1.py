class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_dict = dict()
        t_dict = dict()
        for i in s:
            s_dict[i] = 0
        for i in s:
            s_dict[i] += 1
        for j in t:
            t_dict[j] = 0
        for j in t:
            t_dict[j] += 1
        if s_dict == t_dict:
            return True
        else:
            return False
