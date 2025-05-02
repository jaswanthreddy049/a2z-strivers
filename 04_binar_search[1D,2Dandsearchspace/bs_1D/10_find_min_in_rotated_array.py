class Solution(object):
    def findMin(self, nums):
        s=0
        e=len(nums)-1
        result=float('inf')
        while(s<=e):
            mid=(s+e)//2
            if nums[mid]>=nums[s]:
                result=min(result,nums[s])
                s=mid+1
            else:
                result=min(result,nums[mid])
                e=mid-1
        return result

            
        """
        :type nums: List[int]
        :rtype: int
        """
        