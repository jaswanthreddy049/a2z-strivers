"""42. Trapping Rain Water
Solved
Hard
Topics
premium lock icon
Companies
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

 

Example 1:


Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.
Example 2:

Input: height = [4,2,0,3,2,5]
Output: 9
"""
class Solution(object):
    def trap(self, height):
        l=0
        r=len(height)-1
        total=0
        leftmax,rightmax=0,0
        while(l<r):
            if height[l]<=height[r]:
                if height[l]<leftmax:
                    total+=leftmax-height[l]
                else:
                    leftmax=height[l]
                l+=1
            else:
                if height[r]<rightmax:
                    total+=rightmax-height[r]
                else:
                    rightmax=height[r]
                r-=1
        return total
        """
        :type height: List[int]
        :rtype: int
        """
        