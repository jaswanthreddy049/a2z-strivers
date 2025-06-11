"""84. Largest Rectangle in Histogram
Solved
Hard
Topics
premium lock icon
Companies
Given an array of integers heights representing the histogram's bar height where the width of each bar is 1, return the area of the largest rectangle in the histogram.

 

Example 1:


Input: heights = [2,1,5,6,2,3]
Output: 10
Explanation: The above is a histogram where width of each bar is 1.
The largest rectangle is shown in the red area, which has an area = 10 units.
Example 2:


Input: heights = [2,4]
Output: 4"""
class Solution(object):
    def largestRectangleArea(self, heights):
        stack=[]
        n=len(heights)
        nsl=[n]*n
        psl=[-1]*n
        for i in range(n):
            while(stack and heights[stack[-1]]>heights[i]):
                stack.pop()
            if stack :
                psl[i]=stack[-1]
            stack.append(i)
        stack=[]
        for i in range(n-1,-1,-1):
            while(stack and heights[stack[-1]]>=heights[i]):
                stack.pop()
            if stack :
                nsl[i]=stack[-1]
            stack.append(i)
            
        result=0
        for i in range(n):
            result=max(result,heights[i]*(nsl[i]-psl[i]-1))
        return result

        """
        :type heights: List[int]
        :rtype: int
        """
        