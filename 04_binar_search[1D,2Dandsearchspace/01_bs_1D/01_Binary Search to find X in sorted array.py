class Solution(object):
    def search(self, nums, target):
        lo=0
        up=len(nums)-1
        while(lo<=up):
            mid=(lo+up)//2
            if nums[mid]==target:
                return mid
            elif nums[mid]>target:
                up=mid-1
            else:
                lo=mid+1
        return -1