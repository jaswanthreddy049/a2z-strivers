"""930. Binary Subarrays With Sum
Solved
Medium
Topics
premium lock icon
Companies
Given a binary array nums and an integer goal, return the number of non-empty subarrays with a sum goal.

A subarray is a contiguous part of the array.

 

Example 1:

Input: nums = [1,0,1,0,1], goal = 2
Output: 4
Explanation: The 4 subarrays are bolded and underlined below:
[1,0,1,0,1]
[1,0,1,0,1]
[1,0,1,0,1]
[1,0,1,0,1]
Example 2:

Input: nums = [0,0,0,0,0], goal = 0
Output: 15
 

Constraints:"""
class Solution(object):
    def numSubarraysWithSum(self, nums, goal):
        if goal<0:
            return 0
        def res(nums,goal):
            sums=0
            count=0
            l,r=0,0
            while(r<len(nums)):
                sums+=nums[r]
                while sums>goal and l<=r:
                    sums-=nums[l]
                    l+=1
                count+=(r-l+1)
                r+=1
            return count
        return res(nums,goal)-res(nums,goal-1)
        """
        :type nums: List[int]
        :type goal: int
        :rtype: int
        """
        