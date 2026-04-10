class Solution:
    def isPalindrome(self, s: str) -> bool:
        slist = [char for char in s.lower() if char.isalpha() or char.isalnum()] 
        for i in range(len(slist)//2):
            if slist[i] != slist[len(slist)-1-i]:
                return False
        return True
