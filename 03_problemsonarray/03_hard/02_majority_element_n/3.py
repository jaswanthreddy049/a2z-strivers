"""Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times.

 

Example 1:

Input: nums = [3,2,3]
Output: [3]
Example 2:

Input: nums = [1]
Output: [1]
Example 3:

Input: nums = [1,2]
Output: [1,2]
"""
class Solution(object):
    def majorityElement(self, nums):
        sol=len(nums)//3
        freq={}
        res=[]
        for i in nums:
            if i in freq:
                freq[i]+=1
            else:
                freq[i]=1
            if freq[i]==sol+1:
                res.append(i)
        return res
                    
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        