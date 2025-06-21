"""136. Single Number
Solved
Easy
Topics
premium lock icon
Companies
Hint
Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

You must implement a solution with a linear runtime complexity and use only constant extra space."""
class Solution(object):
    def singleNumber(self, nums):
        xor=nums[0]
        for i in range(1,len(nums)):
            xor=xor^nums[i]
        return xor

        """
        :type nums: List[int]
        :rtype: int
        """
        