"""
Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

 

Example 1:

Input: nums = [3,2,3]
Output: 3
Example 2:

Input: nums = [2,2,1,1,1,2,2]
Output: 2

"""class Solution(object):
    def majorityElement(self, nums):
        freq={}
        maj=len(nums)//2
        for i in nums:
            if i in freq:
                freq[i]+=1
            else:
                freq[i]=1
        for i in freq:
            if freq[i]>maj:
                return i
        """
        :type nums: List[int]
        :rtype: int
        """
        