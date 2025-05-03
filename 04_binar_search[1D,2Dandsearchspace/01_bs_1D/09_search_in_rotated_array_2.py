class Solution(object):
    def search(self, nums, target):
        start=0
        end=len(nums)-1
        while(start<=end):
            mid=(start+end)//2
            if nums[mid]==target:
                return True
            if nums[start]==nums[mid]==nums[end]:
                start+=1
                end-=1
            elif nums[mid]>=nums[start]:
                if nums[mid]>=target and target>=nums[start]:
                    end=mid-1
                else:
                    start=mid+1
            else:
                if nums[mid]<=target and target<=nums[end]:
                    start=mid+1
                else:
                    end=mid-1
        return False
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        