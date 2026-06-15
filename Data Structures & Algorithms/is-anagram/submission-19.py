class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        store = [0]*26
        for i in range(len(s)):
            store[ord(s[i])-ord('a')]+=1
            store[ord(t[i])-ord('a')]-=1
        for val in store:
            if val !=0:
                return False
        return True



        