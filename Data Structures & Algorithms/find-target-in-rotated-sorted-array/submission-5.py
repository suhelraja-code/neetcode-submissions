class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r=0, len(nums)-1
        while l<r:
            mid=(l+r)//2
            if nums[mid]>nums[r]:
                l=mid+1
            else:
                r=mid
        pivote=l

        def binarys(l, r):
            while l<=r:
                mid=(l+r)//2
                if target==nums[mid]:
                    return mid
                else:
                    if target<nums[mid]:
                        r=mid-1
                    else:
                        l=mid+1
            return -1
        res=binarys(0, pivote-1)
        if res!=-1:
            return res
        return binarys(pivote, len(nums)-1)
