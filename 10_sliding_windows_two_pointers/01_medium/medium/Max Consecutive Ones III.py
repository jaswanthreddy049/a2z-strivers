"""1004. Max Consecutive Ones III
Solved
Medium
Topics
premium lock icon
Companies
Hint
Given a binary array nums and an integer k, return the maximum number of consecutive 1's in the array if you can flip at most k 0's.

 

Example 1:

Input: nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2
Output: 6
Explanation: [1,1,1,0,0,1,1,1,1,1,1]
Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.
Example 2:

Input: nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], k = 3
Output: 10
Explanation: [0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1]
Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.
"""
class Solution(object):
    def longestOnes(self, nums, k):
        l=0
        ans=0
        zero=0
        r=0
        while(r<len(nums)):
            if nums[r]==0:
                zero+=1
            if zero>k:
                while(nums[l]!=0):
                    l+=1
                zero-=1
                l+=1
            ans=max(ans,r-l+1)
            r+=1
        return ans

                



        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        