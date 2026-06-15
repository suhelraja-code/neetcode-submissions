class Solution:
    def isValid(self, s: str) -> bool:
        valid=[]
        hash={"}":"{",")":"(","]":"["}
        for i in s:
            if i in ("[{("):
                valid.append(i)
            else:
                if not valid or hash[i] != valid[-1]:
                    return False
                valid.pop()
        return len(valid)==0

