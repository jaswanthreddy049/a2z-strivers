"""Example 1:

Input: nums = [1,0,-1,0,-2,2], target = 0
Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
"""
class Solution(object):
    def fourSum(self, nums, target):
        nums.sort()
        result=[]
        for i in range(len(nums)-1):
            if i>0 and nums[i]==nums[i-1]:continue
            for j in range(i+1,len(nums)-1):
                if j!=i+1 and nums[j]==nums[j-1]:continue
                k=j+1
                l=len(nums)-1
                while(k<l):
                    sums=nums[i]+nums[j]+nums[k]+nums[l]
                    if sums<target:
                        k+=1
                    elif sums>target:
                        l-=1
                    else:
                        temp=[nums[i],nums[j],nums[k],nums[l]]
                        result.append(temp)
                        k+=1
                        l-=1
                        while(k<l and nums[k]==nums[k-1]):k+=1
                        while(k<l and nums[l]==nums[l+1]):l-=1
        return result
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        