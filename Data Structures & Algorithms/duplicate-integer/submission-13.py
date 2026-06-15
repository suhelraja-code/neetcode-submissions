class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dic ={}
        for i in nums:
            dic[i] = 1
        return len(dic) < len(nums)