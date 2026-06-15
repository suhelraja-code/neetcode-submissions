class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list)
        for c in strs:
            a = [0]*26
            for i in c:
                a[ord(i)-ord('a')]+=1
            result[tuple(a)].append(c)
        return list(result.values())