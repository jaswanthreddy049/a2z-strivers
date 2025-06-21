"""78. Subsets
Solved
Medium
Topics
premium lock icon
Companies
Given an integer array nums of unique elements, return all possible subsets (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.

 

"""
class Solution(object):
    def subsets(self, nums):
        total=1<<len(nums)
        ans=[]
        for i in range(total):
            temp=[]
            for j in range(len(nums)):
                if i & 1<<j:
                    temp.append(nums[j])
            ans.append(temp)
        return ans
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        