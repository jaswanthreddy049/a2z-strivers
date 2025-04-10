"""Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.

 

Example 1:

Input: nums = [1,3,5,6], target = 5
Output: 2
Example 2:

Input: nums = [1,3,5,6], target = 2
Output: 1
Example 3:

Input: nums = [1,3,5,6], target = 7
Output: 4
 """
 class Solution(object):
    def searchInsert(self, nums, target):
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
        return lo
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        