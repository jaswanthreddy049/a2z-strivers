"""Given an array nums, return true if the array was originally sorted in non-decreasing order, then rotated some number of positions (including zero). Otherwise, return false.

There may be duplicates in the original array.

Note: An array A rotated by x positions results in an array B of the same length such that B[i] == A[(i+x) % A.length] for every valid index i.

 

Example 1:

Input: nums = [3,4,5,1,2]
Output: true
Explanation: [1,2,3,4,5] is the original sorted array.
You can rotate the array by x = 3 positions to begin on the element of value 3: [3,4,5,1,2].
Example 2:""""
class Solution(object):
    def check(self, nums):
        count=0
        maxi=len(nums)-1
        for i in range(maxi):
            if nums[i]>nums[i+1]:
                count+=1
                if nums[maxi]>nums[0]:
                    return False
        if count<=1:
            return True
        return False


        
        """
        :type nums: List[int]
        :rtype: bool
        """
        