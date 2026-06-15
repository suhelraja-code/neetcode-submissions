class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dic={}
        dic2={}
        i=0
        j=0
        if len(s)!=len(t):
            return False
        return sorted(s)==sorted(t)
