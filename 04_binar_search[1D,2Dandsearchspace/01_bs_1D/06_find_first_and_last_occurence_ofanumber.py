"""34. Find First and Last Position of Element in Sorted Array
Solved
Medium
Topics
Companies
Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.

If target is not found in the array, return [-1, -1].

You must write an algorithm with O(log n) runtime complexity.

 

Example 1:

Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]
Example 2:

Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]"""
class Solution(object):
    def searchRange(self, nums, target):
        def first(nums,target):
            index=-1
            s=0
            e=len(nums)-1
            while(s<=e):
                mid=(s+e)//2
                if nums[mid]>target:
                    e=mid-1
                elif nums[mid]<target:
                    s=mid+1
                else:
                    index=mid
                    e=mid-1
            return index
        def last(nums,target,s):
            index1=-1
            e=len(nums)-1
            while(s<=e):
                mid=(s+e)//2
                if nums[mid]>target:
                    e=mid-1
                elif nums[mid]<target:
                    s=mid+1
                else:
                    index1=mid
                    s=mid+1
            return index1
        start=first(nums,target)
        if start==-1:
            return [-1,-1]
        end=last(nums,target,start)
        return [start,end]
                
        
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        