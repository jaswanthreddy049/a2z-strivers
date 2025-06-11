"""907. Sum of Subarray Minimums
Solved
Medium
Topics
premium lock icon
Companies
Given an array of integers arr, find the sum of min(b), where b ranges over every (contiguous) subarray of arr. Since the answer may be large, return the answer modulo 109 + 7.

 

Example 1:

Input: arr = [3,1,2,4]
Output: 17
Explanation: 
Subarrays are [3], [1], [2], [4], [3,1], [1,2], [2,4], [3,1,2], [1,2,4], [3,1,2,4]. 
Minimums are 3, 1, 2, 4, 1, 1, 2, 1, 1, 1.
Sum is 17.
Example 2:

Input: arr = [11,81,94,43,3]
Output: 444
"""
class Solution(object):
    def sumSubarrayMins(self, arr):
        mod=10**9+7
        n=len(arr)
        nexts=[n]*n
        prevs=[-1]*n
        stack=[]
        for i in range(n):
            while(stack and arr[stack[-1]]>arr[i]):
                stack.pop()
            if stack:prevs[i]=stack[-1]
            else:prevs[i]=-1
            stack.append(i)
        stack=[]
        for i in range(n-1,-1,-1):
            while(stack and arr[stack[-1]]>=arr[i]):
                stack.pop()
            if stack:nexts[i]=stack[-1]
            else:nexts[i]=n
            stack.append(i)
        result=0
        for i in range(n):
            left=i-prevs[i]
            right=nexts[i]-i
            result=((result+left*right*arr[i])%mod)%mod
        return result

        
        """
        :type arr: List[int]
        :rtype: int
        """
        